load Rails.root.join("app", "models", "setting.rb")

class Setting
  class << self
    alias_method :consul_defaults, :defaults

    # Change this code when you'd like to add settings that aren't
    # already present in the database. These settings will be added when
    # first installing CONSUL DEMOCRACY, when deploying code with Capistrano,
    # or when manually executing the `settings:add_new_settings` task.
    #
    # If a setting already exists in the database, changing its value in
    # this file will have no effect unless the task `rake db:seed` is
    # invoked or the method `Setting.reset_defaults` is executed. Doing
    # so will overwrite the values of all existing settings in the
    # database, so use with care.
    #
    # The tests in the spec/ folder rely on CONSUL DEMOCRACY's default
    # settings, so it's recommended not to change the default settings
    # in the test environment.
    def defaults
      if Rails.env.test?
        consul_defaults
      else
        consul_defaults.merge({
          # Overwrite default CONSUL DEMOCRACY settings or add new settings here
          "feature.facebook_login": false,
          "feature.google_login": false,
          "feature.twitter_login": false,
          "feature.user.recommendations": false,
          "feature.user.recommendations_on_debates": false,
          "feature.user.recommendations_on_proposals": false,
          "feature.user.skip_verification": false,
          "feature.community": false,
          "feature.map": true,
          "feature.sdg": false,
          "feature.cookies_consent": true,
          "homepage.widgets.feeds.debates": false,
          "homepage.widgets.feeds.processes": false,
          "homepage.widgets.feeds.proposals": false,
          "locales.enabled": "es val",
          "locales.default": "es",
          "map.latitude": 39.4697989,
          "map.longitude": -0.3774215,
          "map.zoom": 14,
          "map.feature.marker_clustering": false,
          "process.debates": false,
          "process.proposals": false,
          "process.polls": false,
          "process.budgets": true,
          "process.legislation": false,
          "uploads.images.title.min_length": 4,
          "uploads.images.title.max_length": 38,
          "uploads.images.min_width": 475,
          "uploads.images.min_height": 475,
          comments_body_max_length: 6000,
          proposal_code_prefix: "VLCParticipa",
          votes_for_proposal_success: 10000,
          org_name: "VLCParticipa",
          postal_codes: "46001:46026,46035,46112,46131,46135,28013",
          "sdg.process.debates": false,
          "sdg.process.proposals": false,
          "sdg.process.polls": false,
          "sdg.process.budgets": false,
          "sdg.process.legislation": false
        })
      end
    end
  end
end
