from ..models.new_models.administrator import NewAdministrator
from ..models.old_models.administrator import OldAdministrator


async def migrate(id_maps):
    # new fields:
    #   new_administrator.description
    user_map = id_maps["users"]
    id_maps["administrators"] = {}
    old_administrators = await OldAdministrator.all()
    new_administrators = {v.user_id: v for v in await NewAdministrator.all()}
    for old_administrator in old_administrators:
        new_administrator = new_administrators.get(user_map[old_administrator.user_id])
        if new_administrator is None:
            new_administrator = OldAdministrator(
                user_id=user_map[old_administrator.user_id]
            )

        await new_administrator.save()
        id_maps["administrators"][old_administrator.id] = new_administrator.id
