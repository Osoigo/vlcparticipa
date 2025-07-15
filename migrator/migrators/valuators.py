from ..models.new_models.valuator import NewValuator
from ..models.old_models.valuator import OldValuator


async def migrate(id_maps):
    # missing in new:
    #   old_valuator.spending_proposals_count
    #
    # new fields:
    #   new_valuator.can_comment
    #   new_valuator.can_edit_dossier
    user_map = id_maps["users"]
    id_maps["valuators"] = {}
    old_valuators = await OldValuator.all()
    new_valuators = {v.user_id: v for v in await NewValuator.all()}
    for old_valuator in old_valuators:
        new_valuator = new_valuators.get(user_map[old_valuator.user_id])
        if new_valuator is None:
            new_valuator = NewValuator(user_id=user_map[old_valuator.user_id])

        new_valuator.description = old_valuator.description
        new_valuator.budget_investments_count = old_valuator.budget_investments_count
        new_valuator.valuator_group_id = old_valuator.valuator_group_id
        await new_valuator.save()
        id_maps["valuators"][old_valuator.id] = new_valuator.id
