from datetime import datetime

from tortoise import connections

from ..models.new_models.budget_investment import (
    NewBudgetInvestment,
    NewBudgetInvestmentTranslation,
)
from ..models.old_models.budget_investment import OldBudgetInvestment


async def migrate(id_maps, migration_stats):
    # missing in new:
    #   old_budget_investment.unidad
    #   old_budget_investment.proposed_service  (not used in the database)
    #   old_budget_investment.other_services
    #   old_budget_investment.price_phase1
    #   old_budget_investment.price_phase2
    #   old_budget_investment.price_phase3
    #   old_budget_investment.price_phase4
    #   old_budget_investment.budget_implementation
    # new fields:
    #   new_budget_investment.original_heading_id (same as heading_id for this migration)

    # Investments must keep their previous id, but keep id_map to track investment migrations
    id_maps["budget_investments"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
        "missing_admins": set(),
    }
    old_budget_investments = await OldBudgetInvestment.all()
    new_budget_investments = {b.id: b for b in await NewBudgetInvestment.all()}
    new_budget_investment_translations = {
        t.budget_investment_id: t for t in await NewBudgetInvestmentTranslation.all()
    }
    for old_budget_investment in old_budget_investments:
        stats["total"] += 1
        new_budget_investment = new_budget_investments.get(old_budget_investment.id)
        if new_budget_investment is None:
            new_budget_investment = NewBudgetInvestment(id=old_budget_investment.id)
            new_budget_investment_translation = NewBudgetInvestmentTranslation(
                locale="es"
            )
        else:
            new_budget_investment_translation = new_budget_investment_translations[
                new_budget_investment.id
            ]

        new_budget_investment.author_id = id_maps["users"][
            str(old_budget_investment.author_id)
        ]
        if old_budget_investment.administrator_id:
            admin_id = id_maps["administrators"].get(
                str(old_budget_investment.administrator_id)
            )
            if admin_id is None:
                # print(f"missing admin old id: {old_budget_investment.administrator_id}")
                stats["missing_admins"].add(old_budget_investment.administrator_id)
            else:
                new_budget_investment.administrator_id = admin_id
        new_budget_investment.external_url = old_budget_investment.external_url
        new_budget_investment.price = old_budget_investment.price
        new_budget_investment.feasibility = old_budget_investment.feasibility
        new_budget_investment.price_explanation = (
            old_budget_investment.price_explanation
        )
        new_budget_investment.unfeasibility_explanation = (
            old_budget_investment.unfeasibility_explanation
        )
        new_budget_investment.valuation_finished = (
            old_budget_investment.valuation_finished
        )
        new_budget_investment.price_first_year = old_budget_investment.price_first_year
        new_budget_investment.duration = old_budget_investment.duration
        new_budget_investment.hidden_at = old_budget_investment.hidden_at
        new_budget_investment.cached_votes_up = old_budget_investment.cached_votes_up
        new_budget_investment.comments_count = old_budget_investment.comments_count
        new_budget_investment.confidence_score = old_budget_investment.confidence_score
        new_budget_investment.physical_votes = old_budget_investment.physical_votes
        new_budget_investment.tsv = old_budget_investment.tsv
        new_budget_investment.created_at = old_budget_investment.created_at
        new_budget_investment.updated_at = old_budget_investment.updated_at
        new_budget_investment.heading_id = id_maps["budget_headings"][
            str(old_budget_investment.heading_id)
        ]
        new_budget_investment.responsible_name = old_budget_investment.responsible_name
        new_budget_investment.budget_id = id_maps["budgets"][
            str(old_budget_investment.budget_id)
        ]
        new_budget_investment.group_id = id_maps["budget_groups"][
            str(old_budget_investment.group_id)
        ]
        new_budget_investment.selected = old_budget_investment.selected
        new_budget_investment.location = old_budget_investment.location
        new_budget_investment.organization_name = (
            old_budget_investment.organization_name
        )
        new_budget_investment.unfeasible_email_sent_at = (
            old_budget_investment.unfeasible_email_sent_at
        )
        new_budget_investment.ballot_lines_count = (
            old_budget_investment.ballot_lines_count
        )
        new_budget_investment.previous_heading_id = new_budget_investment.heading_id
        new_budget_investment.winner = old_budget_investment.winner
        new_budget_investment.incompatible = old_budget_investment.incompatible
        if old_budget_investment.community_id is not None:
            new_budget_investment.community_id = id_maps["communities"][
                str(old_budget_investment.community_id)
            ]
        else:
            new_budget_investment.community_id = None
        new_budget_investment.visible_to_valuators = (
            old_budget_investment.visible_to_valuators
        )
        new_budget_investment.valuator_group_assignments_count = (
            old_budget_investment.valuator_group_assignments_count
        )
        new_budget_investment.confirmed_hide_at = (
            old_budget_investment.confirmed_hide_at
        )
        new_budget_investment.ignored_flag_at = old_budget_investment.ignored_flag_at
        new_budget_investment.flags_count = old_budget_investment.flags_count
        new_budget_investment.original_heading_id = new_budget_investment.heading_id

        await new_budget_investment.save()

        new_budget_investment_translation.budget_investment_id = (
            new_budget_investment.id
        )
        new_budget_investment_translation.title = old_budget_investment.title
        new_budget_investment_translation.description = (
            old_budget_investment.description
        )
        new_budget_investment_translation.created_at = datetime.now()
        new_budget_investment_translation.updated_at = datetime.now()

        await new_budget_investment_translation.save()
        stats["migrated"] += 1
        id_maps["budget_investments"][str(old_budget_investment.id)] = (
            new_budget_investment.id
        )

    # rebuild budget_investments_id_seq
    connection = connections.get("new")
    await connection.execute_query(
        """SELECT SETVAL('public."budget_investments_id_seq"', COALESCE(MAX(id), 1)) FROM public."budget_investments";"""
    )

    stats["missing_admins"] = list(stats["missing_admins"])
    migration_stats["budget_investments"] = stats
