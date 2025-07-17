from datetime import datetime

from ..models.new_models.budget_group import NewBudgetGroup, NewBudgetGroupTranslation
from ..models.old_models.budget_group import OldBudgetGroup


async def migrate(id_maps):
    id_maps["budget_groups"] = {}
    old_budget_groups = await OldBudgetGroup.all()
    new_budget_groups = {b.slug: b for b in await NewBudgetGroup.all()}
    new_budget_group_translations = {
        t.budget_group_id: t for t in await NewBudgetGroupTranslation.all()
    }
    for old_budget_group in old_budget_groups:
        new_budget_group = new_budget_groups.get(old_budget_group.slug)
        if new_budget_group is None:
            new_budget_group = NewBudgetGroup(slug=old_budget_group.slug)
            new_budget_group_translation = NewBudgetGroupTranslation(locale="es")
        else:
            new_budget_group_translation = new_budget_group_translations[
                new_budget_group.id
            ]

        new_budget_group.budget_id = id_maps["budgets"][str(old_budget_group.budget_id)]
        new_budget_group.max_votable_headings = old_budget_group.max_votable_headings

        await new_budget_group.save()

        new_budget_group_translation.budget_group_id = new_budget_group.id
        new_budget_group_translation.name = old_budget_group.name
        new_budget_group_translation.created_at = datetime.now()
        new_budget_group_translation.updated_at = datetime.now()
        await new_budget_group_translation.save()

        id_maps["budget_groups"][str(old_budget_group.id)] = new_budget_group.id
