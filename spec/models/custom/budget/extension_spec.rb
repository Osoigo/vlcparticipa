require "rails_helper"

describe Budget::Extension do
  describe "#stats_override_content" do
    it "stores translatable HTML stats content" do
      extension = create(:budget).create_extension!(stats_override_content: "<p>Stats</p>")

      expect(extension.stats_override_content).to eq("<p>Stats</p>")
    end
  end

  describe "#stats_override?" do
    it "is false by default" do
      extension = create(:budget).create_extension!

      expect(extension.stats_override?).to be false
    end

    it "is true when the column is set" do
      extension = create(:budget).create_extension!(stats_override: true)

      expect(extension.stats_override?).to be true
    end
  end
end
