class AddEvaluationFieldsToBudgetInvestments  < ActiveRecord::Migration[7.0]
  def change
    add_column :budget_investments, :unidad, :string
    add_column :budget_investments, :other_services, :string
    add_column :budget_investments, :allows_phase, :boolean
    add_column :budget_investments, :price_phase1, :float
    add_column :budget_investments, :price_phase2, :float
    add_column :budget_investments, :price_phase3, :float
    add_column :budget_investments, :price_phase4, :float
    add_column :budget_investments, :budget_implementation, :string
  end
end
