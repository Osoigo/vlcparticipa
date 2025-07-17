from ..models.new_models.milestone import (
    NewMilestoneStatus,
    NewMilestone,
    NewMilestoneTranslation,
)
from ..models.old_models.budget_investment_milestone import (
    OldBudgetInvestmentStatus,
    OldBudgetInvestmentMilestone,
    OldBudgetInvestmentMilestoneTranslation,
)


async def migrate(id_maps):
    # new fields:
    id_maps["milestone_statuses"] = {}
    old_milestone_statuses = await OldBudgetInvestmentStatus.all()
    new_milestone_statuses = {b.name: b for b in await NewMilestoneStatus.all()}
    for old_milestone_status in old_milestone_statuses:
        new_milestone_status = new_milestone_statuses.get(old_milestone_status.name)
        if new_milestone_status is None:
            new_milestone_status = NewMilestoneStatus(name=old_milestone_status.name)

        new_milestone_status.description = old_milestone_status.description
        new_milestone_status.hidden_at = old_milestone_status.hidden_at
        new_milestone_status.created_at = old_milestone_status.created_at
        new_milestone_status.updated_at = old_milestone_status.updated_at
        await new_milestone_status.save()
        id_maps["milestone_statuses"][str(old_milestone_status.id)] = (
            new_milestone_status.id
        )

    id_maps["milestones"] = {}
    old_milestones = await OldBudgetInvestmentMilestone.all()
    new_milestones = {
        (m.milestoneable_id, m.created_at): m for m in await NewMilestone.all()
    }
    old_milestone_translations = {
        t.budget_investment_milestone_id: t
        for t in await OldBudgetInvestmentMilestoneTranslation.all()
    }
    new_milestone_translations = {
        t.milestone_id: t for t in await NewMilestoneTranslation.all()
    }
    for old_milestone in old_milestones:
        old_milestone_translation = old_milestone_translations.get(old_milestone.id)
        if old_milestone_translation is None:
            print(f"missing translation for milestone {old_milestone.id}")
            continue
        new_milestone = new_milestones.get(
            (
                id_maps["budget_investments"][str(old_milestone.investment_id)],
                old_milestone.created_at,
            )
        )
        if new_milestone is None:
            new_milestone = NewMilestone(
                milestoneable_type="Budget::Investment",
                milestoneable_id=id_maps["budget_investments"][
                    str(old_milestone.investment_id)
                ],
                created_at=old_milestone.created_at,
            )
            new_milestone_translation = NewMilestoneTranslation(locale="es")
        else:
            new_milestone_translation = new_milestone_translations[new_milestone.id]

        new_milestone.publication_date = old_milestone.publication_date
        if old_milestone.status_id is not None:
            new_milestone.status_id = id_maps["milestone_statuses"][
                str(old_milestone.status_id)
            ]
        else:
            new_milestone.status_id = None
        new_milestone.updated_at = old_milestone.updated_at

        await new_milestone.save()

        new_milestone_translation.milestone_id = new_milestone.id
        new_milestone_translation.created_at = old_milestone_translation.created_at
        new_milestone_translation.updated_at = old_milestone_translation.updated_at
        new_milestone_translation.title = old_milestone_translation.title
        new_milestone_translation.description = old_milestone_translation.description
        await new_milestone_translation.save()

        id_maps["milestones"][str(old_milestone.id)] = new_milestone.id
