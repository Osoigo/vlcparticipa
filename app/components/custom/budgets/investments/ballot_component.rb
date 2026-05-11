class Budgets::Investments::BallotComponent < ApplicationComponent; end

load Rails.root.join("app", "components", "budgets", "investments", "ballot_component.rb")

class Budgets::Investments::BallotComponent
  private

    def negative_vote_allowed
      budget.negative_votes > 0
    end

    def negative_voted?
      ballot.has_negative_investment?(investment)
    end

    def negative_reason
      @negative_reason ||= investment.reason_for_not_being_negatively_ballotable_by(current_user, ballot)
    end

    def negative_vote_aria_label
      t("budgets.investments.investment.add_negative_label", investment: investment.title)
    end

    def remove_negative_vote_aria_label
      t("budgets.ballots.show.remove_negative_label", investment: investment.title)
    end

    def cannot_vote_text
      if reason.present? && !voted?
        t("budgets.ballots.reasons_for_not_balloting.#{reason}",
          verify_account: link_to_verify_account,
          my_heading: link_to_my_heading,
          change_ballot: link_to_change_ballot,
          heading_link: heading_link(assigned_heading, budget))
      elsif negative_reason.present? && !negative_voted?
        t("budgets.ballots.reasons_for_not_balloting.#{negative_reason}",
          verify_account: link_to_verify_account,
          my_heading: link_to_my_heading,
          change_ballot: link_to_change_ballot,
          heading_link: heading_link(assigned_heading, budget))
      end
    end
end
