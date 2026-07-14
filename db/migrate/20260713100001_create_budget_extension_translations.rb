class CreateBudgetExtensionTranslations < ActiveRecord::Migration[7.0]
  def change
    create_table :budget_extension_translations do |t|
      t.integer :budget_extension_id, null: false
      t.string :locale, null: false
      t.text :stats_override_content

      t.timestamps

      t.index :budget_extension_id
      t.index :locale
    end
  end
end
