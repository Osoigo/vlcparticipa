require "rails_helper"

describe Admin::SiteCustomization::Pages::OrderTableComponent,
         controller: Admin::SiteCustomization::PagesController do
  it "does not render when there are no pages" do
    render_inline Admin::SiteCustomization::Pages::OrderTableComponent.new(SiteCustomization::Page.none)

    expect(page).not_to be_rendered
  end

  it "renders a row for each page in the given order, with a link to the order path" do
    first_page = create(:site_customization_page, :published, :display_in_more_info,
                        title: "First page", slug: "first-page")
    second_page = create(:site_customization_page, :published, :display_in_more_info,
                         title: "Second page", slug: "second-page")

    render_inline Admin::SiteCustomization::Pages::OrderTableComponent.new(
      SiteCustomization::Page.where(id: [first_page.id, second_page.id]).order(:id)
    )

    order_pages_path = Rails.application.routes.url_helpers.admin_site_customization_pages_order_pages_path
    expect(page).to have_css("tbody[data-js-url='#{order_pages_path}']")

    rows = page.all("tbody tr")
    expect(rows.map { |row| row["data-page-id"] }).to eq [first_page.id.to_s, second_page.id.to_s]
    expect(rows[0]).to have_content "First page"
    expect(rows[1]).to have_content "Second page"
  end
end
