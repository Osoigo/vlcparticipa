require "rails_helper"

describe "SDG Goals" do
  before do
    Setting["feature.sdg"] = true
    Setting["sdg.process.debates"] = true
    Setting["sdg.process.proposals"] = true
  end

  describe "Index" do
    scenario "has cards for phases" do
      create(:widget_card, cardable: SDG::Phase["planning"], title: "Planning card")

      visit sdg_goals_path

      within "#sdg_phase_planning" do
        expect(page).to have_css "header", exact_text: "Planning"
        expect(page).to have_content "Planning card"
      end
    end
  end
end
