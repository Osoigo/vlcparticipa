from ..models.new_models.budget_valuator_assignment import NewBudgetValuatorAssignment
from ..models.old_models.budget_valuator_assignment import OldBudgetValuatorAssignment


async def migrate(id_maps):
    id_maps["budget_valuator_assignments"] = {}
    old_assignments = await OldBudgetValuatorAssignment.all()
    new_assignments = {
        (a.valuator_id, a.investment_id): a
        for a in await NewBudgetValuatorAssignment.all()
    }
    for old_assignment in old_assignments:
        new_valuator_id = id_maps["valuators"].get(old_assignment.valuator_id)
        if new_valuator_id is None:
            continue  # This valuator no longer exists, ignore valuator assignment
        new_assignment = new_assignments.get(
            (
                new_valuator_id,
                id_maps["budget_investments"][old_assignment.investment_id],
            )
        )
        if new_assignment is None:
            new_assignment = NewBudgetValuatorAssignment(
                valuator_id=id_maps["valuators"][old_assignment.valuator_id],
                investment_id=id_maps["budget_investments"][
                    old_assignment.investment_id
                ],
            )

        new_assignment.created_at = old_assignment.created_at
        new_assignment.updated_at = old_assignment.updated_at
        await new_assignment.save()
        id_maps["budget_valuator_assignments"][old_assignment.id] = new_assignment.id
