require "rails_helper"

describe "Budget stats override" do
  let(:budget) { create(:budget, :finished) }

  context "when stats_override is active" do
    before do
      budget.create_extension!(stats_override: true, stats_override_content: "<p>Stats content</p>")
    end

    scenario "shows override HTML instead of the generated stats" do
      visit budget_stats_path(budget)

      expect(page).to have_content("Stats content")
    end

    scenario "does not render the stats sidebar" do
      visit budget_stats_path(budget)

      expect(page).not_to have_css ".sidebar"
    end
  end

  context "when stats_override is inactive" do
    scenario "shows the normal stats content" do
      visit budget_stats_path(budget)

      expect(page).to have_css ".stats-content"
    end
  end
end
