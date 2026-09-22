load Rails.root.join("app", "models", "site_customization", "page.rb")

class SiteCustomization::Page
  scope :sort_by_position, -> { order(:position, :id) }
  scope :with_more_info_flag, -> { where(status: "published", more_info_flag: true).sort_by_position }

  def self.order_pages(ordered_array)
    ordered_array.each_with_index do |page_id, index|
      find(page_id).update_column(:position, index + 1)
    end
  end
end
