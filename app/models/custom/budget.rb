load Rails.root.join("app", "models", "budget.rb")

class Budget
  def negative_votes?
    negative_votes > 0
  end
end
