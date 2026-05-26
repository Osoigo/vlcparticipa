require "rails_helper"

describe "Cards", :admin do
  context "Header Card" do
    context "Page card" do
      let!(:custom_page) { create(:site_customization_page, :published) }

      scenario "Show label only if it is present" do
        card_1 = create(:widget_card, cardable: custom_page, title: "Card one", label: "My label")
        card_2 = create(:widget_card, cardable: custom_page, title: "Card two")

        visit custom_page.url

        within("#widget_card_#{card_1.id}") do
          expect(page).to have_css "span", text: "My label"
        end

        within("#widget_card_#{card_2.id}") do
          expect(page).not_to have_css "span"
        end
      end

      scenario "Show image if it is present" do
        card_1 = create(:widget_card, cardable: custom_page, title: "Card one")
        card_2 = create(:widget_card, cardable: custom_page, title: "Card two")

        card_1.update!(image: create(:image,
                                     imageable: card_1,
                                     attachment: fixture_file_upload("clippy.jpg")))
        card_2.update!(image: nil)

        visit custom_page.url

        within(".card", text: "Card one") { expect(page).to have_css "img" }
        within(".card", text: "Card two") { expect(page).not_to have_css "img" }
      end
    end
  end
end
