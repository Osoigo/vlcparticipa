load Rails.root.join("app", "controllers", "valuation", "budget_investments_controller.rb")

class Valuation::BudgetInvestmentsController
  alias_method :consul_allowed_params, :allowed_params

  def allowed_params
    consul_allowed_params + [
      :unidad, :other_services, :budget_implementation, :allows_phase,
      :price_phase1, :price_phase2, :price_phase3, :price_phase4
    ]
  end
end
