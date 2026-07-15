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

  describe "#extension_for_editing" do
    it "builds a new extension when the budget doesn't have one" do
      budget = create(:budget)

      expect(budget.extension_for_editing).to be_a(Budget::Extension).and be_new_record
    end

    it "returns the existing extension" do
      budget = create(:budget)
      extension = budget.create_extension!(stats_override: true)

      expect(budget.extension_for_editing).to eq(extension)
    end

    it "pre-builds a translation, not marked for destruction, for every locale the budget already uses" do
      budget = create(:budget)
      budget.update!(name_fr: "Nom en français")

      translations = budget.extension_for_editing.translations

      expect(translations.map(&:locale)).to contain_exactly(*budget.locales_not_marked_for_destruction)
      expect(translations.map(&:marked_for_destruction?)).to all(be false)
    end

    it "doesn't pre-build translations again for an already persisted extension" do
      budget = create(:budget)
      budget.update!(name_fr: "Nom en français")
      budget.create_extension!(stats_override: true)

      expect(budget.extension_for_editing.translations).to be_empty
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
