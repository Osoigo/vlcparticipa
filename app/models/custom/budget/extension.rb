class Budget
  class Extension < ApplicationRecord
    belongs_to :budget

    translates :stats_override_content
    include Globalizable
  end
end
