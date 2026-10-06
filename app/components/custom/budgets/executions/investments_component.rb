class Budgets::Executions::InvestmentsComponent < ApplicationComponent
  delegate :markdown, to: :helpers
end

load Rails.root.join("app", "components", "budgets", "executions", "investments_component.rb")

class Budgets::Executions::InvestmentsComponent < ApplicationComponent
end
