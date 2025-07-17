class AddWebServiceFieldsToUsers < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :nIA, :string
    add_column :users, :name, :string
    add_column :users, :first_name, :string
    add_column :users, :last_name, :string
    add_column :users, :municipality_of_birth, :string
    add_column :users, :province_of_birth, :string
    add_column :users, :country_of_birth, :string
    add_column :users, :nationality, :integer
    add_column :users, :dc, :string
    add_column :users, :census_last_modification_at, :date
    add_column :users, :district, :integer
    add_column :users, :section, :integer
    add_column :users, :sheet_number, :string
    add_column :users, :census_created_at, :date
    add_column :users, :collective_entity, :string
    add_column :users, :singular_entity, :string
    add_column :users, :core, :string
    add_column :users, :single_entity_code, :string
    add_column :users, :census_phone, :string, limit: 30
    add_column :users, :level_of_training, :string
    add_column :users, :permit_expiration_at, :date
    add_column :users, :province, :string
    add_column :users, :municipality, :string
    add_column :users, :acronym, :string
    add_column :users, :type_road, :string
    add_column :users, :street_name, :string
    add_column :users, :access, :string
    add_column :users, :km, :string
    add_column :users, :stairs, :string
    add_column :users, :floor, :string
    add_column :users, :door, :string
    add_column :users, :zip_code, :string
    add_column :users, :full_address, :string
    add_column :users, :protected_hab, :boolean
  end
end
