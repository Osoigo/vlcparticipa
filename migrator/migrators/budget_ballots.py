from tortoise.functions import Count

from ..models.new_models.budget_ballot import (
    NewBudgetBallot,
    NewBudgetBallotLine,
    NewBudgetBallotNegativeline,
)
from ..models.new_models.budget_investment import NewBudgetInvestment
from ..models.old_models.budget_ballot import (
    OldBudgetBallot,
    OldBudgetBallotLine,
    OldBudgetBallotNegativeline,
)


async def migrate(id_maps, migration_stats):
    # missing in new:
    #   old_budget_ballot.ballot_old
    #
    # new fields:
    #   new_budget_ballot.ballot_lines_count, done
    #   new_budget_ballot.ballot_negativelines_count, done
    #   new_budget_ballot.physical
    #   new_budget_ballot.poll_ballot_id
    #
    #   new_budget_ballot_line.budget_id, done
    #   new_budget_ballot_line.group_id, done
    #   new_budget_ballot_line.heading_id, done
    id_maps["budget_ballots"] = {}
    stats = {
        "ballots": {
            "total": 0,
            "migrated": 0,
            "missing_users": set(),
            "not_migrated_ballots": set(),
        },
        "lines": {
            "total": 0,
            "migrated": 0,
            "missing_ballots": set(),
        },
        "negativelines": {
            "total": 0,
            "migrated": 0,
            "missing_ballots": set(),
        },
    }
    old_budget_ballots = await OldBudgetBallot.all()
    total_old_ballots = len(old_budget_ballots)
    new_budget_ballots = {
        (b.user_id, b.budget_id, b.created_at): b for b in await NewBudgetBallot.all()
    }
    for idx, old_budget_ballot in enumerate(old_budget_ballots):
        stats["ballots"]["total"] += 1
        user_id = id_maps["users"].get(str(old_budget_ballot.user_id))
        if user_id is None:
            # print(
            #     f"Missing user, old_ballot_id: {old_budget_ballot.id} old user_id: {old_budget_ballot.user_id}"
            # )
            stats["ballots"]["not_migrated_ballots"].add(old_budget_ballot.id)
            stats["ballots"]["missing_users"].add(old_budget_ballot.user_id)
            continue
        new_budget_ballot = new_budget_ballots.get(
            (
                user_id,
                id_maps["budgets"][str(old_budget_ballot.budget_id)],
                old_budget_ballot.created_at,
            )
        )
        if new_budget_ballot is None:
            new_budget_ballot = NewBudgetBallot(
                user_id=id_maps["users"][str(old_budget_ballot.user_id)],
                budget_id=id_maps["budgets"][str(old_budget_ballot.budget_id)],
                created_at=old_budget_ballot.created_at,
            )
        new_budget_ballot.updated_at = old_budget_ballot.updated_at
        await new_budget_ballot.save()
        stats["ballots"]["migrated"] += 1
        id_maps["budget_ballots"][str(old_budget_ballot.id)] = new_budget_ballot.id
        print(f"{idx} / {total_old_ballots }", end="\r")

    investment_data_map = {
        i.id: (i.budget_id, i.group_id, i.heading_id)
        for i in await NewBudgetInvestment.all()
    }
    id_maps["budget_ballot_lines"] = {}
    old_budget_ballot_lines = await OldBudgetBallotLine.all()
    new_budget_ballot_lines = {
        (b.ballot_id, b.investment_id): b for b in await NewBudgetBallotLine.all()
    }
    for old_budget_ballot_line in old_budget_ballot_lines:
        stats["lines"]["total"] += 1
        ballot_id = id_maps["budget_ballots"].get(str(old_budget_ballot_line.ballot_id))
        if ballot_id is None:
            # print(f"Missing ballot. Old id: {old_budget_ballot_line.ballot_id}")
            stats["lines"]["missing_ballots"].add(old_budget_ballot_line.ballot_id)
            continue
        new_budget_ballot_line = new_budget_ballot_lines.get(
            (
                ballot_id,
                id_maps["budget_investments"][
                    str(old_budget_ballot_line.investment_id)
                ],
            )
        )
        if new_budget_ballot_line is None:
            new_budget_ballot_line = NewBudgetBallotLine(
                ballot_id=id_maps["budget_ballots"][
                    str(old_budget_ballot_line.ballot_id)
                ],
                investment_id=id_maps["budget_investments"][
                    str(old_budget_ballot_line.investment_id)
                ],
            )
        new_budget_ballot_line.created_at = old_budget_ballot_line.created_at
        new_budget_ballot_line.updated_at = old_budget_ballot_line.updated_at
        budget_id, group_id, heading_id = investment_data_map[
            id_maps["budget_investments"][str(old_budget_ballot_line.investment_id)]
        ]
        new_budget_ballot_line.budget_id = budget_id
        new_budget_ballot_line.group_id = group_id
        new_budget_ballot_line.heading_id = heading_id
        await new_budget_ballot_line.save()
        stats["lines"]["migrated"] += 1
        id_maps["budget_ballot_lines"][str(old_budget_ballot_line.id)] = (
            new_budget_ballot_line.id
        )

    #   new_budget_ballot_line.heading_id
    ballot_lines_count = (
        await NewBudgetBallotLine.annotate(count=Count("id"))
        .group_by("ballot_id")
        .values("ballot_id", "count")
    )
    for entry in ballot_lines_count:
        await NewBudgetBallot.filter(id=entry["ballot_id"]).update(
            ballot_lines_count=entry["count"]
        )

    id_maps["budget_ballot_negativelines"] = {}
    old_budget_ballot_negativelines = await OldBudgetBallotNegativeline.all()
    new_budget_ballot_negativelines = {
        (b.ballot_id, b.investment_id): b
        for b in await NewBudgetBallotNegativeline.all()
    }
    for old_budget_ballot_negativeline in old_budget_ballot_negativelines:
        stats["negativelines"]["total"] += 1
        ballot_id = id_maps["budget_ballots"].get(
            str(old_budget_ballot_negativeline.ballot_id)
        )
        if ballot_id is None:
            # print(f"Missing ballot. Old id: {old_budget_ballot_line.ballot_id}")
            stats["lines"]["missing_ballots"].add(
                old_budget_ballot_negativeline.ballot_id
            )
            continue
        new_budget_ballot_negativeline = new_budget_ballot_negativelines.get(
            (
                ballot_id,
                id_maps["budget_investments"][
                    str(old_budget_ballot_negativeline.investment_id)
                ],
            )
        )
        if new_budget_ballot_negativeline is None:
            new_budget_ballot_negativeline = NewBudgetBallotNegativeline(
                ballot_id=id_maps["budget_ballots"][
                    str(old_budget_ballot_negativeline.ballot_id)
                ],
                investment_id=id_maps["budget_investments"][
                    str(old_budget_ballot_negativeline.investment_id)
                ],
            )
        new_budget_ballot_negativeline.created_at = (
            old_budget_ballot_negativeline.created_at
        )
        new_budget_ballot_negativeline.updated_at = (
            old_budget_ballot_negativeline.updated_at
        )
        budget_id, group_id, heading_id = investment_data_map[
            id_maps["budget_investments"][
                str(old_budget_ballot_negativeline.investment_id)
            ]
        ]
        new_budget_ballot_negativeline.budget_id = budget_id
        new_budget_ballot_negativeline.group_id = group_id
        new_budget_ballot_negativeline.heading_id = heading_id
        await new_budget_ballot_negativeline.save()
        stats["negativelines"]["migrated"] += 1
        id_maps["budget_ballot_negativelines"][
            str(old_budget_ballot_negativeline.id)
        ] = new_budget_ballot_negativeline.id

    # ballot_negativelines_count = (
    #     await NewBudgetBallotNegativeline.annotate(count=Count("id"))
    #     .group_by("ballot_id")
    #     .values("ballot_id", "count")
    # )
    # for entry in ballot_negativelines_count:
    #     await NewBudgetBallot.filter(id=entry["ballot_id"]).update(
    #         ballot_negativelines_count=entry["count"]
    #     )

    stats["ballots"]["missing_users"] = list(stats["ballots"]["missing_users"])
    stats["ballots"]["not_migrated_ballots"] = list(
        stats["ballots"]["not_migrated_ballots"]
    )
    stats["lines"]["missing_ballots"] = list(stats["lines"]["missing_ballots"])
    stats["negativelines"]["missing_ballots"] = list(
        stats["negativelines"]["missing_ballots"]
    )
    migration_stats["budget_ballots"] = stats
