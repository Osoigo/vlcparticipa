class Budgets::Ballot::NegativeInvestmentComponent < Budgets::Ballot::InvestmentComponent
  def initialize(negative_investment:)
    @investment = negative_investment
  end

  private

    def delete_path
      budget_ballot_negativeline_path(budget, id: investment.id)
    end
end
