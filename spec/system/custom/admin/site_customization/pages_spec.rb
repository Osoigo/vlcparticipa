require "rails_helper"

describe "Admin site customization pages order", :admin do
  scenario "Reorders pages listed in the more information page via drag and drop" do
    first = create(:site_customization_page, :published, :display_in_more_info,
                   slug: "first", title_en: "First page")
    second = create(:site_customization_page, :published, :display_in_more_info,
                    slug: "second", title_en: "Second page")

    visit admin_site_customization_pages_path

    within(".more-info-pages-order-table tbody") do
      expect("First page").to appear_before("Second page")

      find("tr", text: "Second page").drag_to(find("tr", text: "First page"))

      expect("Second page").to appear_before("First page")
    end

    Timeout.timeout(Capybara.default_max_wait_time) do
      sleep 0.1 until second.reload.position && first.reload.position && second.position < first.position
    end

    refresh

    within(".more-info-pages-order-table tbody") do
      expect("Second page").to appear_before("First page")
    end
  end

  scenario "Does not show the order table when there are no pages flagged for more info" do
    create(:site_customization_page, :published, slug: "not-flagged", more_info_flag: false)

    visit admin_site_customization_pages_path

    expect(page).not_to have_css ".more-info-pages-order-table"
  end
end
