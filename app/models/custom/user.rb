load Rails.root.join("app", "models", "user.rb")

class User
  def can_vote_budget_investment_for_this_budget?(budget_id)
    vote_registers = Vote.where(voter_id: id, votable_type: "Budget::Investment", vote_flag: true)
    max_votes_setting = Setting.where(key: "max_votes_per_budget_per_user")
    return true if max_votes_setting.empty? # El parametro max_votes_per_budget_per_user no existe

    max_votes_setting = max_votes_setting.first.value.to_i
    i = 0
    vote_registers.find_each do |vote|
      if vote&.votable&.budget_id == budget_id # Comprobamos que el voto pertenece a budget_id
        i += 1
      end
      # No hace falta seguir comprobando si hemos alcanzado el limite
      return false if i >= max_votes_setting # El usuario ha votado limite veces.
    end
    true
  end
end
