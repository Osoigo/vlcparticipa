class AddResultsExtensionToBudgetExtensions < ActiveRecord::Migration[7.0]
  def change
    add_column :budget_extensions, :results_extension, :boolean, default: false, null: false
    add_column :budget_extension_translations, :results_extension_content, :text
  end
end
