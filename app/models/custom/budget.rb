load Rails.root.join("app", "models", "budget.rb")

class Budget
  has_one :extension, class_name: "Budget::Extension", dependent: :destroy
  accepts_nested_attributes_for :extension

  delegate :stats_override?, :stats_override_content, to: :extension, allow_nil: true

  def negative_votes?
    negative_votes > 0
  end
end
