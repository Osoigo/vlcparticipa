load Rails.root.join("app", "models", "budget.rb")

class Budget
  has_one :extension, class_name: "Budget::Extension", dependent: :destroy
  accepts_nested_attributes_for :extension

  delegate :stats_override?, :stats_override_content,
           :results_extension?, :results_extension_content,
           to: :extension, allow_nil: true

  def extension_for_editing
    ext = extension || build_extension
    existing_locales = ext.translations.map(&:locale)

    locales_not_marked_for_destruction.each do |locale|
      ext.translations.build(locale: locale) unless existing_locales.include?(locale)
    end

    ext
  end

  def negative_votes?
    negative_votes > 0
  end
end
