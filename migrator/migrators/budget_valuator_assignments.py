from ..models.new_models.budget_valuator_assignment import NewBudgetValuatorAssignment
from ..models.old_models.budget_valuator_assignment import OldBudgetValuatorAssignment


async def migrate(id_maps, migration_stats):
    id_maps["budget_valuator_assignments"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_assignments = await OldBudgetValuatorAssignment.all()
    new_assignments = {
        (a.valuator_id, a.investment_id): a
        for a in await NewBudgetValuatorAssignment.all()
    }
    for old_assignment in old_assignments:
        stats["total"] += 1
        new_valuator_id = id_maps["valuators"].get(str(old_assignment.valuator_id))
        if new_valuator_id is None:
            continue  # This valuator no longer exists, ignore valuator assignment
        investment_id = id_maps["budget_investments"].get(
            str(old_assignment.investment_id)
        )
        if investment_id is None:
            print(f"missing investment, old_id: {old_assignment.investment_id}")
            continue
        new_assignment = new_assignments.get(
            (
                new_valuator_id,
                investment_id,
            )
        )
        if new_assignment is None:
            valuator_id = id_maps["valuators"][str(old_assignment.valuator_id)]
            new_assignment = NewBudgetValuatorAssignment(
                valuator_id=valuator_id,
                investment_id=id_maps["budget_investments"][
                    str(old_assignment.investment_id)
                ],
            )

        new_assignment.created_at = old_assignment.created_at
        new_assignment.updated_at = old_assignment.updated_at

        await new_assignment.save()
        stats["migrated"] += 1
        id_maps["budget_valuator_assignments"][str(old_assignment.id)] = (
            new_assignment.id
        )

    migration_stats["budget_valuator_assignments"] = stats
