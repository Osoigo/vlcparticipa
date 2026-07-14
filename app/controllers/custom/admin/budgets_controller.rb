load Rails.root.join("app", "controllers", "admin", "budgets_controller.rb")

class Admin::BudgetsController
  alias_method :consul_allowed_params, :allowed_params

  def allowed_params
    consul_allowed_params + [
      :negative_votes,
      :negative_vote_value,
      extension_attributes: [
        :id,
        :stats_override,
        translation_params(Budget::Extension)
      ]
    ]
  end

  def set_winners_form
  end

  def set_winners
    return unless @budget.balloting_finished?

    file_data = params[:csvfile]
    if file_data.respond_to?(:read)
      contents = file_data.read
    elsif file_data.respond_to?(:path)
      contents = File.read(file_data.path)
    else
      return
    end

    @budget.investments.update_all(winner: false)
    winner_investments = []
    missing_investment_ids = []
    contents.split("\n").each do |line|
      investment_id = line.strip
      begin
        winner_investments << Budget::Investment.find(investment_id)
      rescue ActiveRecord::RecordNotFound
        missing_investment_ids << investment_id
      end
    end

    winner_investments.each do |investment|
      investment.update(winner: true)
    end
    if missing_investment_ids.size > 0
      alert_msg = I18n.t("admin.budgets.winners.missing_winner_ids", count: missing_investment_ids.size)
      alert_msg = "%s: %s " % [alert_msg, missing_investment_ids.join(" , ")]
      redirect_to admin_budget_budget_investments_path(budget_id: @budget.id, filter: "winners"),
                  alert:  alert_msg
    else
      redirect_to admin_budget_budget_investments_path(budget_id: @budget.id, filter: "winners"),
                  notice: I18n.t("admin.budgets.winners.done")
    end
  end
end
