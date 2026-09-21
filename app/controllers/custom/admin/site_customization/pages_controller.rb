load Rails.root.join("app", "controllers", "admin", "site_customization", "pages_controller.rb")

class Admin::SiteCustomization::PagesController
  def order_pages
    SiteCustomization::Page.order_pages(params[:ordered_list])
    head :ok
  end
end
