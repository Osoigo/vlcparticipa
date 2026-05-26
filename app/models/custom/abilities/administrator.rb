load Rails.root.join("app", "models", "abilities", "administrator.rb")

module Abilities
  class Administrator
    alias_method :consul_initialize, :initialize

    def initialize(user)
      consul_initialize(user)
      can [:set_winners_form, :set_winners], Budget
    end
  end
end
