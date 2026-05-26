load Rails.root.join("app", "controllers", "concerns", "admin", "budget_headings_actions.rb")

module Admin::BudgetHeadingsActions
  private

    alias_method :consul_allowed_params, :allowed_params

    def allowed_params
      consul_allowed_params + [:required_support]
    end
end
