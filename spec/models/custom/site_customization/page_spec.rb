require "rails_helper"

describe SiteCustomization::Page do
  describe ".with_more_info_flag" do
    it "orders pages by position, breaking ties by id" do
      third = create(:site_customization_page, :published, :display_in_more_info, slug: "third", position: 2)
      first = create(:site_customization_page, :published, :display_in_more_info, slug: "first", position: 0)
      second_a = create(:site_customization_page, :published, :display_in_more_info,
                        slug: "second-a", position: 1)
      second_b = create(:site_customization_page, :published, :display_in_more_info,
                        slug: "second-b", position: 1)

      expect(SiteCustomization::Page.with_more_info_flag).to eq [first, second_a, second_b, third]
    end

    it "keeps today's order (by id) when no page has a position yet" do
      first = create(:site_customization_page, :published, :display_in_more_info, slug: "first")
      second = create(:site_customization_page, :published, :display_in_more_info, slug: "second")

      expect(first.position).to be(nil)
      expect(second.position).to be(nil)
      expect(SiteCustomization::Page.with_more_info_flag).to eq [first, second]
    end

    it "sorts pages without a position (nil) after positioned pages" do
      not_positioned = create(:site_customization_page, :published, :display_in_more_info,
                              slug: "not-positioned")
      positioned = create(:site_customization_page, :published, :display_in_more_info,
                          slug: "positioned", position: 0)

      expect(SiteCustomization::Page.with_more_info_flag).to eq [positioned, not_positioned]
    end

    it "excludes pages not flagged for more info" do
      create(:site_customization_page, :published, more_info_flag: false)

      expect(SiteCustomization::Page.with_more_info_flag).to be_empty
    end

    it "excludes draft pages even if flagged for more info" do
      create(:site_customization_page, :display_in_more_info, status: "draft")

      expect(SiteCustomization::Page.with_more_info_flag).to be_empty
    end
  end

  describe ".order_pages" do
    it "sets positions following the given order, starting at 1" do
      first = create(:site_customization_page, :published, :display_in_more_info, slug: "first")
      second = create(:site_customization_page, :published, :display_in_more_info, slug: "second")
      third = create(:site_customization_page, :published, :display_in_more_info, slug: "third")

      SiteCustomization::Page.order_pages([third.id, first.id, second.id])

      expect(third.reload.position).to eq 1
      expect(first.reload.position).to eq 2
      expect(second.reload.position).to eq 3
    end

    it "persists the new order for .with_more_info_flag" do
      first = create(:site_customization_page, :published, :display_in_more_info, slug: "first")
      second = create(:site_customization_page, :published, :display_in_more_info, slug: "second")

      SiteCustomization::Page.order_pages([second.id, first.id])

      expect(SiteCustomization::Page.with_more_info_flag).to eq [second, first]
    end
  end
end
