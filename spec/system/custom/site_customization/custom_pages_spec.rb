require "rails_helper"

describe "Custom Pages" do
  context "New custom page" do
    context "Published" do
      scenario "Show widget cards for that page" do
        custom_page = create(:site_customization_page, :published)
        create(:widget_card, cardable: custom_page, title: "Medium prominent card", order: 2)
        create(:widget_card, cardable: custom_page, title: "Less prominent card", order: 2)
        create(:widget_card, cardable: custom_page, title: "Card Highlights", order: 1)

        visit custom_page.url

        expect("Card Highlights").to appear_before("Medium prominent card")
        expect("Medium prominent card").to appear_before("Less prominent card")
      end
    end
  end
end
