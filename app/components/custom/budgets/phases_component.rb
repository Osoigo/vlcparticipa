class Budgets::PhasesComponent < ApplicationComponent; end

load Rails.root.join("app", "components", "budgets", "phases_component.rb")

class Budgets::PhasesComponent
  delegate :image_path_for, to: :helpers
end
