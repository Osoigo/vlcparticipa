from tortoise import connections

from ..models.new_models.budget import NewBudget, NewBudgetTranslation
from ..models.old_models.budget import OldBudget


async def migrate(id_maps, migration_stats):
    # missing in new:
    #   old_budget.vote_types  ('all' en todos los buckets de producción)
    #   old_budget.description_waiting
    #
    # new fields:
    #   new_budget.voting_style
    #   new_budget.published
    #   new_budget.hide_money
    #   new_budget_translations.main_link_text
    #   new_budget_translations.main_link_url
    id_maps["budgets"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_budgets = await OldBudget.all()
    new_budgets = {b.slug: b for b in await NewBudget.all()}
    new_budget_translations = {t.budget_id: t for t in await NewBudgetTranslation.all()}
    for old_budget in old_budgets:
        stats["total"] += 1
        new_budget = new_budgets.get(old_budget.slug)
        if new_budget is None:
            new_budget = NewBudget(slug=old_budget.slug)
            new_budget_translation = NewBudgetTranslation(id=old_budget.id, locale="es")
        else:
            new_budget_translation = new_budget_translations[new_budget.id]

        new_budget.currency_symbol = old_budget.currency_symbol
        if old_budget.phase == "drafting":
            old_budget.phase = "accepting"
        else:
            new_budget.published = True
        new_budget.phase = old_budget.phase
        new_budget.created_at = old_budget.created_at
        new_budget.updated_at = old_budget.updated_at
        new_budget.description_accepting = old_budget.description_accepting
        new_budget.description_reviewing = old_budget.description_reviewing
        new_budget.description_valuating = old_budget.description_valuating
        new_budget.description_balloting = old_budget.description_balloting
        new_budget.description_reviewing_ballots = (
            old_budget.description_reviewing_ballots
        )
        new_budget.description_finished = old_budget.description_finished
        new_budget.description_drafting = old_budget.description_drafting
        new_budget.description_publishing_prices = (
            old_budget.description_publishing_prices
        )
        new_budget.description_informing = old_budget.description_informing

        await new_budget.save()

        new_budget_translation.budget_id = new_budget.id
        new_budget_translation.name = old_budget.name
        new_budget_translation.created_at = old_budget.created_at
        new_budget_translation.updated_at = old_budget.updated_at
        new_budget_translation.negative_votes = old_budget.negative_votes
        new_budget_translation.negative_vote_value = old_budget.negative_vote_value

        await new_budget_translation.save()
        stats["migrated"] += 1
        id_maps["budgets"][str(old_budget.id)] = new_budget.id

    # rebuild budgets_id_seq
    connection = connections.get("new")
    await connection.execute_query(
        """SELECT SETVAL('public."budgets_id_seq"', COALESCE(MAX(id), 1)) FROM public."budgets";"""
    )

    migration_stats["budgets"] = stats
