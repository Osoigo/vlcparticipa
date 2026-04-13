require "rails_helper"

describe "Admin budget investments", :admin do
  let(:budget) { create(:budget) }
  let(:administrator) do
    create(:administrator, user: create(:user, username: "Ana", email: "ana@admins.org"))
  end

  context "Selecting xlsx", :no_js do
    scenario "Downloading XLSX file" do
      admin = create(:administrator, user: create(:user, username: "Admin"))
      valuator = create(:valuator, user: create(:user, username: "Valuator"))
      valuator_group = create(:valuator_group, name: "Valuator Group")
      budget_group = create(:budget_group, name: "Budget Group", budget: budget)
      first_budget_heading = create(:budget_heading, group: budget_group, name: "Budget Heading")
      second_budget_heading = create(:budget_heading, group: budget_group, name: "Other Heading")
      create(:budget_investment, :feasible, :selected, title: "Le Investment",
                                                       budget: budget, group: budget_group,
                                                       heading: first_budget_heading,
                                                       cached_votes_up: 88, price: 99,
                                                       valuators: [],
                                                       valuator_groups: [valuator_group],
                                                       administrator: admin,
                                                       visible_to_valuators: true)
      create(:budget_investment, :unfeasible, title: "Alt Investment",
                                              budget: budget, group: budget_group,
                                              heading: second_budget_heading,
                                              cached_votes_up: 66, price: 88,
                                              valuators: [valuator],
                                              valuator_groups: [],
                                              visible_to_valuators: false)

      visit admin_budget_budget_investments_path(budget)

      click_link "Download XLSX"

      header = page.response_headers["Content-Disposition"]
      expect(header).to match(/^attachment/)
      expect(header).to match(/filename="Propuestas de inversión.xlsx"/)
    end
  end

  context "Show" do
    scenario "Show the investment details" do
      user = create(:user, username: "Rachel", email: "rachel@valuators.org")
      valuator = create(:valuator, user: user)
      budget_investment = create(:budget_investment,
                                 :unfeasible,
                                 unfeasibility_explanation: "It is impossible",
                                 price: 1234,
                                 administrator: administrator,
                                 valuators: [valuator])

      visit admin_budget_budget_investments_path(budget_investment.budget)

      within_window(window_opened_by { click_link budget_investment.title }) do
        expect(page).to have_content("Investment preview")
        expect(page).to have_content(budget_investment.title)
        expect(page).to have_content(budget_investment.description)
        expect(page).to have_content(budget_investment.author.name)
        expect(page).to have_content(budget_investment.heading.name)
        expect(page).to have_content("1234")
        expect(page).to have_content("Unfeasible")
        expect(page).to have_content("It is impossible")
        expect(page).to have_content("Ana (ana@admins.org)")

        within("#assigned_valuators") do
          expect(page).to have_content("Rachel (rachel@valuators.org)")
        end

        expect(page).to have_button "Publish comment"
      end
    end

    scenario "Show image and documents on investment details" do
      budget_investment = create(:budget_investment,
                                 :with_image,
                                 :unfeasible,
                                 unfeasibility_explanation: "It is impossible",
                                 price: 1234,
                                 administrator: administrator)
      document = create(:document, documentable: budget_investment)

      visit admin_budget_budget_investments_path(budget_investment.budget)

      within_window(window_opened_by { click_link budget_investment.title }) do
        expect(page).to have_content(budget_investment.title)
        expect(page).to have_content(budget_investment.description)
        expect(page).to have_content(budget_investment.author.name)
        expect(page).to have_content(budget_investment.heading.name)
        expect(page).to have_content("Investment preview")
        expect(page).to have_content(budget_investment.image.title)
        expect(page).to have_content("Documents (1)")
        expect(page).to have_link text: document.title
        expect(page).to have_content("1234")
        expect(page).to have_content("Unfeasible")
        expect(page).to have_content("It is impossible")
        expect(page).to have_content("Ana (ana@admins.org)")
      end
    end
  end

  context "Columns chooser" do
    let!(:investment) do
      create(:budget_investment,
             :winner,
             :visible_to_valuators,
             budget: budget,
             author: create(:user, username: "Jon Doe"))
    end

    scenario "Set cookie with default columns value if undefined", :consul do
      visit admin_budget_budget_investments_path(budget)

      cookie_value = cookie_by_name("investments-columns")[:value]

      expect(cookie_value).to eq("id,title,created_at,supports,votes,admin,geozone,feasibility," \
                                 "price,valuation_finished,visible_to_valuators,selected,incompatible")
    end

    scenario "Cookie will be updated after change columns selection" do
      investment.winner # call investment to avoid rubocop error, the test fails if no investment available

      visit admin_budget_budget_investments_path(budget)

      click_button "Columns"

      expect(page).to have_css "button[aria-expanded=true]", exact_text: "Columns"

      within("#js-columns-selector-wrapper") do
        uncheck "Title"
        uncheck "Price"
        uncheck "Valuation Group / Valuator"
        uncheck "Created at"
        check "Author"
      end

      cookie_value = cookie_by_name("investments-columns")[:value]

      expect(cookie_value).to eq("id,supports,votes,admin,geozone,feasibility," \
                                 "valuation_finished,visible_to_valuators,selected,incompatible,author")

      refresh

      expect(page).to have_css "button[aria-expanded=false]", exact_text: "Columns"

      cookie_value = cookie_by_name("investments-columns")[:value]

      expect(cookie_value).to eq("id,supports,votes,admin,geozone,feasibility," \
                                 "valuation_finished,visible_to_valuators,selected,incompatible,author")
    end
  end
end
