require "rails_helper"

describe "Localization" do
  scenario "Wrong locale" do
    I18n.with_locale(:es) do
      create(:widget_card, title: "Bienvenido a CONSUL",
                           description: "Software libre para la participación ciudadana.",
                           link_text: "Más información",
                           link_url: "http://consuldemocracy.org/",
                           header: true)
    end

    visit root_path(locale: :es)
    visit root_path(locale: :klingon)

    expect(page).to have_text("BIENVENIDO A CONSUL")
  end
end
