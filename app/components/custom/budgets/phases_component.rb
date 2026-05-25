class Budgets::PhasesComponent < ApplicationComponent; end

load Rails.root.join("app", "components", "budgets", "phases_component.rb")

class Budgets::PhasesComponent
  use_helpers :image_path_for
end
