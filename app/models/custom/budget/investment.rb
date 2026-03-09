load Rails.root.join("app", "models", "budget", "investment.rb")

class Budget
  class Investment
    # Add sort by ballots
    SORTING_OPTIONS = { id: "id", supports: "cached_votes_up", ballots: "ballot_lines_count" }.freeze


    def self.advanced_filters(params, results)
      # Add filter by comments
      results = results.without_admin      if params[:advanced_filters].include?("without_admin")
      results = results.without_valuator   if params[:advanced_filters].include?("without_valuator")
      results = results.under_valuation    if params[:advanced_filters].include?("under_valuation")
      results = results.valuation_finished if params[:advanced_filters].include?("valuation_finished")
      results = results.winners            if params[:advanced_filters].include?("winners")

      ids = []
      ids += results.valuation_finished_feasible.ids if params[:advanced_filters].include?("feasible")
      ids += results.where(selected: true).ids       if params[:advanced_filters].include?("selected")
      ids += results.undecided.ids                   if params[:advanced_filters].include?("undecided")
      ids += results.unfeasible.ids                  if params[:advanced_filters].include?("unfeasible")
      ids += results.where("comments_count > 0").ids if params[:advanced_filters].include?('with_comments')
      ids += results.where("comments_count = 0").ids if params[:advanced_filters].include?('without_comments')
      results = results.where(id: ids) if ids.any?
      results
    end
  end
end
