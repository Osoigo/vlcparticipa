from ..models.new_models.lock import NewLock
from ..models.old_models.lock import OldLock


async def migrate(id_maps, migration_stats):
    id_maps["locks"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_locks = await OldLock.all()
    new_locks = {l.created_at: l for l in await NewLock.all()}
    for old_lock in old_locks:
        stats["total"] += 1

        new_lock = new_locks.get(old_lock.created_at)
        if new_lock is None:
            new_lock = NewLock(created_at=old_lock.created_at)

        new_lock.user_id = id_maps["users"][str(old_lock.user_id)]
        new_lock.tries = old_lock.tries
        new_lock.locked_until = old_lock.locked_until
        new_lock.updated_at = old_lock.updated_at

        await new_lock.save()
        stats["migrated"] += 1
        id_maps["locks"][str(old_lock.id)] = new_lock.id

    migration_stats["locks"] = stats
