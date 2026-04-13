class Budget
  class Ballot
    class Negativeline < ActiveRecord::Base
      belongs_to :ballot
      belongs_to :investment, counter_cache: :ballot_negativelines_count
      belongs_to :heading
      belongs_to :group
      belongs_to :budget

      validates :ballot_id, :investment_id, :heading_id, :group_id, :budget_id, presence: true

      validate :check_selected
      validate :check_negatives_available
      validate :check_valid_heading

      scope :by_investment, ->(investment_id) { where(investment_id: investment_id) }

      before_validation :set_denormalized_ids

      def check_negatives_available
        errors.add(:negatives, "No more negative votes available") if budget.negative_votes <= ballot.negativelines.count
      end

      def check_valid_heading
        return if ballot.valid_heading?(heading)
        errors.add(:heading, "This heading's budget is invalid, or a heading on the same group was already selected")
      end

      def check_selected
        errors.add(:investment, "unselected investment") unless investment.selected?
      end

      private

        def set_denormalized_ids
          self.heading_id ||= investment.try(:heading_id)
          self.group_id   ||= investment.try(:group_id)
          self.budget_id  ||= investment.try(:budget_id)
        end
    end
  end
end
