class CreateBudgetExtensions < ActiveRecord::Migration[7.0]
  def change
    create_table :budget_extensions do |t|
      t.integer :budget_id, null: false
      t.boolean :stats_override, default: false, null: false

      t.timestamps
    end

    add_index :budget_extensions, :budget_id, unique: true
  end
end
