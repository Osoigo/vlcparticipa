load Rails.root.join("app", "components", "account", "permissions_list_component.rb")

class Account::PermissionsListComponent
  private

    def permissions
      perms = {}
      perms[t("verification.user_permission_debates")] = true if Setting["process.debates"].present?
      if Setting["process.proposals"].present?
        perms[t("verification.user_permission_proposal")] = true
      end
      if Setting["process.budgets"].present?
        perms[t("verification.user_permission_budget_investment")] = user.level_two_or_three_verified?
      end
      perms[t("verification.user_permission_support_proposal")] = user.level_two_or_three_verified?
      perms[t("verification.user_permission_votes")] = user.level_three_verified?
      perms
    end
end
