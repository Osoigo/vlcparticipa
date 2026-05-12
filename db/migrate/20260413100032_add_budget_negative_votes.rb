class AddBudgetNegativeVotes < ActiveRecord::Migration[7.0]
  def change
    add_column :budgets, :negative_votes, :integer, default: 0
    add_column :budgets, :negative_vote_value, :float, default: 0.5

    create_table :budget_ballot_negativelines do |t|
      t.belongs_to :ballot
      t.belongs_to :budget
      t.belongs_to :group
      t.belongs_to :heading
      t.belongs_to :investment
      t.datetime :created_at, null: false
      t.datetime :updated_at, null: false
    end
    add_index :budget_ballot_negativelines,
              [:ballot_id, :investment_id],
              unique: true,
              name: "index_budget_ballot_negativelines_ballot_and_investment"

    add_column :budget_investments, :ballot_negativelines_count, :integer, default: 0
  end
end
