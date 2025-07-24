from ..models.new_models.manager import NewManager
from ..models.old_models.manager import OldManager


async def migrate(id_maps, migration_stats):
    id_maps["managers"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
        "missing_users": set(),
    }
    old_managers = await OldManager.all()
    new_managers = {v.user_id: v for v in await NewManager.all()}
    for old_manager in old_managers:
        stats["total"] += 1
        user_id = id_maps["users"].get(str(old_manager.user_id))
        if user_id is None:
            # print(f"Missing user. Old id: {old_manager.user_id}")
            stats["missing_users"].add(old_manager.user_id)
            continue
        new_manager = new_managers.get(user_id)
        if new_manager is None:
            new_manager = NewManager(user_id=user_id)
        await new_manager.save()
        stats["migrated"] += 1
        id_maps["managers"][str(old_manager.id)] = new_manager.id

    stats["missing_users"] = list(stats["missing_users"])
    migration_stats["managers"] = stats
