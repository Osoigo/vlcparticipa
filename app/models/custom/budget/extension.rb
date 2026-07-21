class Budget
  class Extension < ApplicationRecord
    belongs_to :budget

    translates :stats_override_content
    translates :results_extension_content
    include Globalizable
  end
end
