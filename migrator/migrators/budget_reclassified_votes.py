from ..models.new_models.budget_reclassified_vote import NewBudgetReclasifiedVote
from ..models.old_models.budget_reclassified_vote import OldBudgetReclasifiedVote


async def migrate(id_maps, migration_stats):
    id_maps["budget_reclassified_votes"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_budget_reclassified_votes = await OldBudgetReclasifiedVote.all()
    new_budget_reclassified_votes = {
        (b.user_id, b.investment_id): b for b in await NewBudgetReclasifiedVote.all()
    }
    for old_budget_reclassified_vote in old_budget_reclassified_votes:
        stats["total"] += 1
        new_budget_reclassified_vote = new_budget_reclassified_votes.get(
            (
                id_maps["users"][str(old_budget_reclassified_vote.user_id)],
                id_maps["budget_investments"][
                    str(old_budget_reclassified_vote.investment_id)
                ],
            )
        )
        if new_budget_reclassified_vote is None:
            new_budget_reclassified_vote = NewBudgetReclasifiedVote(
                user_id=id_maps["users"][str(old_budget_reclassified_vote.user_id)],
                investment_id=id_maps["budget_investments"][
                    str(old_budget_reclassified_vote.investment_id)
                ],
            )

        new_budget_reclassified_vote.reason = old_budget_reclassified_vote.reason
        new_budget_reclassified_vote.created_at = (
            old_budget_reclassified_vote.created_at
        )
        new_budget_reclassified_vote.updated_at = (
            old_budget_reclassified_vote.updated_at
        )

        await old_budget_reclassified_vote.save()

        stats["migrated"] += 1
        id_maps["budget_reclassified_votes"][str(old_budget_reclassified_vote.id)] = (
            new_budget_reclassified_vote.id
        )

    migration_stats["budget_reclassified_votes"] = stats
