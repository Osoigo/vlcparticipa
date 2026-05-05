class Budgets::Ballot::BallotComponent < ApplicationComponent; end

load Rails.root.join("app", "components", "budgets", "ballot", "ballot_component.rb")

class Budgets::Ballot::BallotComponent
  private

    def negative_ballot_groups
      ballot.negativegroups.sort_by_name
    end

    def no_negative_balloted_groups
      budget.groups.sort_by_name - ballot.negativegroups
    end

    def group_negative_investments(group)
      ballot.negativeinvestments.by_group(group.id).joins(:negativelines).sort_by_ballot_negativelines
    end
end
