require "rails_helper"

describe Budget do
  describe "#stats_override?" do
    it "is falsey when there is no extension" do
      expect(create(:budget).stats_override?).to be_falsey
    end

    it "delegates to the extension" do
      budget = create(:budget)
      budget.create_extension!(stats_override: true)

      expect(budget.stats_override?).to be true
    end
  end

  describe "#stats_override_content" do
    it "delegates to the extension" do
      budget = create(:budget)
      budget.create_extension!(stats_override_content: "<p>Stats</p>")

      expect(budget.stats_override_content).to eq("<p>Stats</p>")
    end
  end

  describe "#negative_votes?" do
    it "is false when negative_votes is zero" do
      expect(create(:budget, negative_votes: 0).negative_votes?).to be false
    end

    it "is true when negative_votes is positive" do
      expect(create(:budget, negative_votes: 1).negative_votes?).to be true
    end
  end
end
