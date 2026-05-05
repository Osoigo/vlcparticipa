class Budgets::Investments::MyBallotComponent < ApplicationComponent; end

load Rails.root.join("app", "components", "budgets", "investments", "my_ballot_component.rb")

class Budgets::Investments::MyBallotComponent
  def negated_investments
    ballot.negativeinvestments.by_heading(heading.id).sort_by_ballot_negativelines
  end

  def negated_investment_ids
    negated_investments.ids
  end
end
