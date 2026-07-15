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

  context "with a budget that already uses more than one locale" do
    let(:budget) do
      b = create(:budget)
      b.update!(name_fr: "Nom en français")
      b
    end

    before { Setting["locales.enabled"] = "en fr" }

    scenario "saves stats_override_content for a locale switched to via Current language" do
      visit edit_admin_budget_path(budget)

      check "budget[extension_attributes][stats_override]"
      fill_in_ckeditor "Stats HTML content", with: "Contenido EN"

      # Selects "fr" directly (instead of the "Current language" <select>) because that
      # locale is already listed there (the budget's name is already translated into it),
      # so an admin naturally uses it instead of "Add language" to reach it.
      page.execute_script(<<~JS)
        var el = document.querySelector('.js-select-language');
        el.value = 'fr';
        el.dispatchEvent(new Event('change', { bubbles: true }));
      JS

      fill_in_ckeditor "Stats HTML content", with: "Contenu FR"
      click_button "Update Budget"

      expect(page).to have_content(I18n.t("admin.budgets.update.notice"))

      budget.reload
      translations = budget.extension.translations.index_by(&:locale)

      expect(translations[:en].stats_override_content).to include("Contenido EN")
      expect(translations[:fr].stats_override_content).to include("Contenu FR")
    end
  end
end
