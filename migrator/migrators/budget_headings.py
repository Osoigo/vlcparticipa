from datetime import datetime

from ..models.new_models.budget_heading import (
    NewBudgetHeading,
    NewBudgetHeadingTranslation,
)
from ..models.old_models.budget_heading import OldBudgetHeading


async def migrate(id_maps, migration_stats):
    # new fields:
    #   new_budget_heading.allow_custom_content
    #   new_budget_heading.latitude
    #   new_budget_heading.longitude
    #   new_budget_heading.geozone_id
    #   new_budget_heading.max_ballot_lines
    #   new_budget_heading.created_at
    #   new_budget_heading.updated_at
    id_maps["budget_headings"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_budget_headings = await OldBudgetHeading.all()
    new_budget_headings = {b.slug: b for b in await NewBudgetHeading.all()}
    new_budget_heading_translations = {
        t.budget_heading_id: t for t in await NewBudgetHeadingTranslation.all()
    }
    for old_budget_heading in old_budget_headings:
        stats["total"] += 1
        new_budget_heading = new_budget_headings.get(old_budget_heading.slug)
        if new_budget_heading is None:
            new_budget_heading = NewBudgetHeading(slug=old_budget_heading.slug)
            new_budget_heading_translation = NewBudgetHeadingTranslation(locale="es")
        else:
            new_budget_heading_translation = new_budget_heading_translations[
                new_budget_heading.id
            ]

        new_budget_heading.group_id = id_maps["budget_groups"][
            str(old_budget_heading.group_id)
        ]
        new_budget_heading.price = old_budget_heading.price
        new_budget_heading.population = old_budget_heading.population
        new_budget_heading.required_support = old_budget_heading.required_support

        await new_budget_heading.save()

        new_budget_heading_translation.budget_heading_id = new_budget_heading.id
        new_budget_heading_translation.name = old_budget_heading.name
        new_budget_heading_translation.created_at = datetime.now()
        new_budget_heading_translation.updated_at = datetime.now()

        await new_budget_heading_translation.save()
        stats["migrated"] += 1
        id_maps["budget_headings"][str(old_budget_heading.id)] = new_budget_heading.id

    migration_stats["budget_headings"] = stats
