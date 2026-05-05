load Rails.root.join("app", "models", "budget", "ballot.rb")

class Budget
  class Ballot
    has_many :negativelines, dependent: :destroy
    has_many :negativeinvestments, through: :negativelines, source: :investment
    has_many :negativegroups, -> { distinct }, through: :negativelines, source: :group
    has_many :negativeheadings, -> { distinct }, through: :negativegroups

    def has_negative_investment?(investment)
      negativeinvestment_ids.include?(investment.id)
    end

    def negate_investment(investment)
      negativelines.create(investment: investment).persisted?
    end

    def has_negativelines_in_group?(group)
      negativegroups.include?(group)
    end

    def heading_for_negativegroup(group)
      return nil unless has_negativelines_in_group?(group)
      negativeinvestments.where(group: group).first.heading
    end
  end
end
