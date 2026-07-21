require "rails_helper"

describe Admin::Budgets::FormComponent, :admin do
  describe "stats override section" do
    it "renders the stats_override checkbox" do
      render_inline Admin::Budgets::FormComponent.new(create(:budget))

      expect(page).to have_field "budget[extension_attributes][stats_override]", type: :checkbox
    end

    it "hides the override fields container when stats_override is false" do
      budget = create(:budget)
      budget.create_extension!(stats_override: false)

      render_inline Admin::Budgets::FormComponent.new(budget)

      expect(page).to have_css ".stats-override-fields", visible: :hidden
    end

    it "shows the override fields container when stats_override is true" do
      budget = create(:budget)
      budget.create_extension!(stats_override: true)

      render_inline Admin::Budgets::FormComponent.new(budget)

      expect(page).to have_css ".stats-override-fields", visible: :visible
    end

    it "renders an html-area textarea for the stats content" do
      budget = create(:budget)
      budget.create_extension!(stats_override: true)

      render_inline Admin::Budgets::FormComponent.new(budget)

      expect(page).to have_css "textarea.html-area"
    end
  end
end
