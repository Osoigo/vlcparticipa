load Rails.root.join("app", "controllers", "admin", "budgets_controller.rb")

class Admin::BudgetsController
  alias_method :consul_allowed_params, :allowed_params

  def allowed_params
    consul_allowed_params + [
      :negative_votes, :negative_vote_value
    ]
  end
end
