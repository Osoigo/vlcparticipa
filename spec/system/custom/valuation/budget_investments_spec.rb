require "rails_helper"

describe "Valuation budget investments" do
  let(:budget) { create(:budget, :valuating) }
  let(:valuator) do
    create(:valuator, user: create(:user, username: "Rachel", email: "rachel@valuators.org"))
  end

  before do
    login_as(valuator.user)
  end

  describe "Valuate" do
    let(:admin) { create(:administrator) }
    let(:investment) do
      create(:budget_investment, budget: budget, price: nil, administrator: admin, valuators: [valuator])
    end

    scenario "Dossier empty by default" do
      investment.update!(visible_to_valuators: true)

      visit valuation_budget_budget_investments_path(budget)
      click_link investment.title

      within("#price") { expect(page).to have_content("Undefined") }
      # within("#price_first_year") { expect(page).to have_content("Undefined") }
      within("#duration") { expect(page).to have_content("Undefined") }
      within("#feasibility") { expect(page).to have_content("Undecided") }
      expect(page).not_to have_content("Valuation finished")
    end

    scenario "Edit dossier" do
      investment.update!(visible_to_valuators: true)
      visit valuation_budget_budget_investments_path(budget)
      within("#budget_investment_#{investment.id}") do
        click_link "Edit dossier"
      end

      fill_in "budget_investment_price", with: "12345"
      # fill_in "budget_investment_price_first_year", with: "9876"
      fill_in "budget_investment_price_explanation", with: "Very cheap idea"
      choose  "budget_investment_feasibility_feasible"
      fill_in "budget_investment_duration", with: "19 months"
      check "budget_investment_allows_phase"
      fill_in "budget_investment_price_phase1", with: "1212"
      fill_in "budget_investment_price_phase2", with: "2222"
      fill_in "budget_investment_price_phase3", with: "3232"
      fill_in "budget_investment_price_phase4", with: "4242"
      click_button "Save changes"

      expect(page).to have_content "Dossier updated"

      visit valuation_budget_budget_investments_path(budget)
      click_link investment.title

      within("#price") { expect(page).to have_content("12345") }
      # within("#price_first_year") { expect(page).to have_content("9876") }
      expect(page).to have_content("Very cheap idea")
      within("#duration") { expect(page).to have_content("19 months") }
      within("#feasibility") { expect(page).to have_content("Feasible") }
      expect(page).not_to have_content("Valuation finished")
    end

    scenario "Feasibility selection makes proper fields visible" do
      feasible_fields = [
        "Service executing the proposal", "Other services involved",
        "Comments on the investment proposal", "Price (€)",
        "Budget application", "Time scope"
      ]
      unfeasible_fields = ["Feasibility explanation"]
      any_feasibility_fields = ["Valuation finished"]
      undecided_fields = feasible_fields + unfeasible_fields + any_feasibility_fields

      visit edit_valuation_budget_budget_investment_path(budget, investment)

      expect(find("#budget_investment_feasibility_undecided")).to be_checked

      undecided_fields.each do |field|
        expect(page).to have_content(field)
      end

      choose "budget_investment_feasibility_feasible"

      unfeasible_fields.each do |field|
        expect(page).not_to have_content(field)
      end

      (feasible_fields + any_feasibility_fields).each do |field|
        expect(page).to have_content(field)
      end

      choose "budget_investment_feasibility_unfeasible"

      feasible_fields.each do |field|
        expect(page).not_to have_content(field)
      end

      (unfeasible_fields + any_feasibility_fields).each do |field|
        expect(page).to have_content(field)
      end

      click_button "Save changes"

      expect(page).to have_content "Dossier updated"

      visit edit_valuation_budget_budget_investment_path(budget, investment)

      expect(find("#budget_investment_feasibility_unfeasible")).to be_checked
      feasible_fields.each do |field|
        expect(page).not_to have_content(field)
      end

      (unfeasible_fields + any_feasibility_fields).each do |field|
        expect(page).to have_content(field)
      end

      choose "budget_investment_feasibility_undecided"

      undecided_fields.each do |field|
        expect(page).to have_content(field)
      end
    end

    scenario "Validates price formats on the server side", :no_js do
      investment.update!(visible_to_valuators: true)

      visit edit_valuation_budget_budget_investment_path(budget, investment)

      fill_in "Price (€)", with: "12345,98"
      # fill_in "Cost during the first year (€) (optional, data not public)", with: "9876.6"
      click_button "Save changes"

      expect(page).to have_content("1 error")
      expect(page).to have_content("Only integer numbers", count: 1)
    end
  end
end
