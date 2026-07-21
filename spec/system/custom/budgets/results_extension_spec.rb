require "rails_helper"

describe "Budget results extension" do
  let(:budget) { create(:budget, :finished) }
  let(:group) { create(:budget_group, budget: budget) }
  let(:heading) { create(:budget_heading, group: group, price: 1000) }

  before do
    create(:budget_investment, :selected, heading: heading, price: 200,
                                          ballot_lines_count: 100)
    Budget::Result.new(budget, heading).calculate_winners
  end

  context "when results_extension is active" do
    before do
      budget.create_extension!(results_extension: true,
                               results_extension_content: "<p>Extension content</p>")
    end

    scenario "shows extension HTML below the results table" do
      visit budget_results_path(budget)

      expect(page).to have_content("Extension content")
    end
  end

  context "when results_extension is inactive" do
    scenario "does not show extension content" do
      visit budget_results_path(budget)

      expect(page).not_to have_css ".results-extension"
    end
  end
end
