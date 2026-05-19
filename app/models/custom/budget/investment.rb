load Rails.root.join("app", "models", "budget", "investment.rb")

class Budget
  class Investment
    has_many :negativelines, dependent: :destroy, class_name: "Budget::Ballot::Negativeline"

    # Add sort by ballots
    SORTING_OPTIONS = { id: "id",
                        created_at: "created_at",
                        supports: "cached_votes_up",
                        ballots: "ballot_lines_count",
                        negative_ballots: "ballot_negativelines_count",
                        total_ballots: "(\
                            budget_investments.ballot_lines_count \
                            - budget_investments.ballot_negativelines_count \
                            * budgets.negative_vote_value\
                        )"}.freeze

    # Add created before and after filters
    scope :by_created_after,            ->(date)    { where(budget_investments: { created_at: date.. }) }
    scope :by_created_before,           ->(date)    { where(budget_investments: { created_at: ..date }) }
    scope :enough_support, -> {
      joins(:heading).where(
        "budget_investments.cached_votes_up + budget_investments.physical_votes" \
        " >= budget_headings.required_support"
      )
    }
    scope :sort_by_ballots, -> {
      joins(:budget).reorder(
        Arel.sql(
          "(\
            budget_investments.ballot_lines_count \
            - budget_investments.ballot_negativelines_count \
            * budgets.negative_vote_value\
           ) DESC"
        ),
        "id DESC"
      )
    }
    scope :sort_by_ballot_negativelines, -> { order(:"budget_ballot_negativelines.created_at") }

    class << self
      alias_method :consul_scoped_filter, :scoped_filter
      alias_method :consul_order_filter, :order_filter
    end

    def self.scoped_filter(params, current_filter)
      results = consul_scoped_filter(params, current_filter)
      results = results.by_created_before(params[:created_before]) if params[:created_before].present?
      results = results.by_created_after(params[:created_after]) if params[:created_after].present?
      results
    end

    def self.advanced_filters(params, results)
      # Add filter by comments
      results = results.without_admin      if params[:advanced_filters].include?("without_admin")
      results = results.without_valuator   if params[:advanced_filters].include?("without_valuator")
      results = results.under_valuation    if params[:advanced_filters].include?("under_valuation")
      results = results.valuation_finished if params[:advanced_filters].include?("valuation_finished")
      results = results.winners            if params[:advanced_filters].include?("winners")
      results = results.enough_support     if params[:advanced_filters].include?("enough_support")

      ids = []
      ids += results.valuation_finished_feasible.ids if params[:advanced_filters].include?("feasible")
      ids += results.where(selected: true).ids       if params[:advanced_filters].include?("selected")
      ids += results.undecided.ids                   if params[:advanced_filters].include?("undecided")
      ids += results.unfeasible.ids                  if params[:advanced_filters].include?("unfeasible")
      ids += results.where("comments_count > 0").ids if params[:advanced_filters].include?("with_comments")
      ids += results.where("comments_count = 0").ids if params[:advanced_filters].include?("without_comments")
      results = results.where(id: ids) if ids.any?
      results
    end

    def self.order_filter(params)
      # Added Arel.sql for false dangerous query method on sort by total_ballots
      # Add join to budgets if sorting_key is total_ballots
      sorting_key = params[:sort_by]&.downcase&.to_sym
      allowed_sort_option = SORTING_OPTIONS[sorting_key]
      direction = params[:direction] == "desc" ? "desc" : "asc"

      if allowed_sort_option.present?
        if sorting_key == :total_ballots
          joins(:budget).order(Arel.sql("#{allowed_sort_option} #{direction}"))
        else
          order("#{allowed_sort_option} #{direction}")
        end
      elsif sorting_key == :title
        direction == "asc" ? sort_by_title : sort_by_title.reverse
      else
        order(cached_votes_up: :desc).order(id: :desc)
      end
    end

    def has_required_support?
      if heading.required_support.present?
        return heading.required_support <= total_votes
      end

      false
    end

    def final_score
      ballot_lines_count - ballot_negativelines_count * budget.negative_vote_value
    end

    alias_method :consul_reason_for_not_being_selectable_by, :reason_for_not_being_selectable_by

    def reason_for_not_being_selectable_by(user)
      reason = consul_reason_for_not_being_selectable_by(user)
      if reason.present?
        return reason
      end

      can_vote = user.can_vote_budget_investment_for_this_budget?(budget_id)
      :max_votes_per_budget_per_user_limit_reached unless can_vote
    end

    def reason_for_not_being_negatively_ballotable_by(user, ballot)
      return permission_problem(user)         if permission_problem?(user)
      return :not_selected                    unless selected?
      return :no_ballots_allowed              unless budget.balloting?
      return :different_heading_assigned      unless ballot.valid_heading?(heading)

      :no_negative_ballots_remaining if ballot.present? && !negative_ballots_remaining?(ballot)
    end

    def negative_ballots_remaining?(ballot)
      if budget.negative_votes > 0
        ballot.negativelines.count < budget.negative_votes
      else
        true
      end
    end

    def working_group_investment?
      tags_name = tags.map { |tag| tag.name.upcase }
      tags_name.include?("GRUPO DE TRABAJO POR DISTRITO")
    end
  end
end
