load Rails.root.join("app", "models", "budget", "investment.rb")

class Budget
  class Investment
    SORTING_OPTIONS = { id: "id", supports: "cached_votes_up", ballots: "ballot_lines_count" }.freeze
  end
end
