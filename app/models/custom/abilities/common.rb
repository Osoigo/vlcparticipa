load Rails.root.join("app", "models", "abilities", "common.rb")

module Abilities
  class Common
    alias_method :consul_initialize, :initialize

    def initialize(user)
      consul_initialize(user)

      if user.level_two_or_three_verified?
        can [:create, :destroy], Budget::Ballot::Negativeline, budget: { phase: "balloting" }
      end
    end
  end
end

