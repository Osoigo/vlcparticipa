class AddPositionToSiteCustomizationPages < ActiveRecord::Migration[7.0]
  def change
    add_column :site_customization_pages, :position, :integer
  end
end
