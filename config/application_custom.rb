module Consul
  class Application < Rails::Application
    [
      "app/controllers/custom/concerns",
    ].each do |path|
      config.autoload_paths << Rails.root.join(path)
      config.eager_load_paths << Rails.root.join(path)
    end
  end
end
