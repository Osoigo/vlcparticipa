class AddBudgetNegativeVotes < ActiveRecord::Migration[7.0]
  def change
    add_column :budgets, :negative_votes, :integer, default: 0
    add_column :budgets, :negative_vote_value, :float, default: 0.5

    create_table :budget_ballot_negativelines do |t|
      t.integer :ballot_id, index: true
      t.integer :budget_id, index: true
      t.integer :group_id, index: true
      t.integer :heading_id, index: true
      t.integer :investment_id, index: true
      t.datetime :created_at, null: false
      t.datetime :updated_at, null: false
    end
    add_index :budget_ballot_negativelines, [:ballot_id, :investment_id], unique: true, name: "index_budget_ballot_negativelines_ballot_and_investment"

    add_column :budget_investments, :ballot_negativelines_count, :integer, default: 0
  end
end
