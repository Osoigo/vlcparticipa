require "rails_helper"

describe Admin::SiteCustomization::PagesController do
  describe "POST order_pages" do
    it "orders the pages following the given list" do
      admin = create(:administrator).user
      first = create(:site_customization_page, :display_in_more_info, slug: "first-page")
      second = create(:site_customization_page, :display_in_more_info, slug: "second-page")

      sign_in admin
      post :order_pages, params: { ordered_list: [second.id, first.id] }

      expect(response).to have_http_status(:ok)
      expect(second.reload.position).to eq 1
      expect(first.reload.position).to eq 2
    end

    it "checks permissions to order pages" do
      user = create(:administrator).user
      restricted_ability = user.ability.tap { |ability| ability.cannot :order_pages, SiteCustomization::Page }
      first = create(:site_customization_page, :display_in_more_info, slug: "first-page")
      second = create(:site_customization_page, :display_in_more_info, slug: "second-page")

      sign_in user
      allow(controller).to receive(:current_ability).and_return(restricted_ability)
      post :order_pages, params: { ordered_list: [second.id, first.id] }

      expect(response).to redirect_to "/"
      expect(first.reload.position).to be(nil)
      expect(second.reload.position).to be(nil)
    end
  end
end
