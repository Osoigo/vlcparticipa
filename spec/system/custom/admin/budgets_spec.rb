require "rails_helper"

describe "Admin budget stats override", :admin do
  let(:budget) { create(:budget) }

  scenario "shows stats_override checkbox on edit form" do
    visit edit_admin_budget_path(budget)

    expect(page).to have_field "budget[extension_attributes][stats_override]", type: :checkbox
  end

  scenario "override fields are hidden when stats_override is false" do
    visit edit_admin_budget_path(budget)

    expect(page).to have_css ".stats-override-fields", visible: :hidden
  end

  scenario "override fields become visible when checkbox is checked" do
    visit edit_admin_budget_path(budget)

    check "budget[extension_attributes][stats_override]"

    expect(page).to have_css ".stats-override-fields", visible: :visible
  end

  scenario "saves stats_override flag" do
    visit edit_admin_budget_path(budget)

    check "budget[extension_attributes][stats_override]"
    click_button "Update Budget"

    expect(page).to have_content(I18n.t("admin.budgets.update.notice"))
    expect(budget.reload.stats_override?).to be true
  end
end
