from ..models.new_models.administrator import NewAdministrator
from ..models.old_models.administrator import OldAdministrator


async def migrate(id_maps, migration_stats):
    # new fields:
    #   new_administrator.description
    id_maps["administrators"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_administrators = await OldAdministrator.all()
    new_administrators = {v.user_id: v for v in await NewAdministrator.all()}
    for old_administrator in old_administrators:
        stats["total"] += 1
        new_administrator = new_administrators.get(
            id_maps["users"][str(old_administrator.user_id)]
        )
        if new_administrator is None:
            new_administrator = OldAdministrator(
                user_id=id_maps["users"][str(old_administrator.user_id)]
            )

        await new_administrator.save()
        stats["migrated"] += 1
        id_maps["administrators"][str(old_administrator.id)] = new_administrator.id

    migration_stats["administrators"] = stats
