class Admin::SiteCustomization::Pages::OrderTableComponent < ApplicationComponent
  attr_reader :pages

  def initialize(pages)
    @pages = pages
  end

  def render?
    pages.any?
  end
end
