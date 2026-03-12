require_dependency Rails.root.join("app", "models", "budget", "investment").to_s

class Budget
  class Investment
    scope :enough_support, -> {
      joins(:heading).where(
        "budget_investments.cached_votes_up + budget_investments.physical_votes" \
        " >= budget_headings.required_support"
      )
    }

    def has_required_support?
      if heading.required_support.present?
        return heading.required_support <= total_votes
      end

      false
    end
  end
end
