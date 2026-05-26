load Rails.root.join("app", "components", "admin", "settings", "configuration_tab_component.rb")

class Admin::Settings::ConfigurationTabComponent
  alias_method :consul_settings, :settings

  def settings
    consul_settings + %w[
      max_votes_per_budget_per_user
    ]
  end
end
