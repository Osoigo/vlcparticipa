from ..models.new_models.activity import NewActivity
from ..models.old_models.activity import OldActivity


async def migrate(id_maps, migration_stats):
    id_maps["activities"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_activities = await OldActivity.all()
    new_activities = {
        (a.user_id, a.action, a.actionable_id, a.actionable_type, a.created_at): a
        for a in await NewActivity.all()
    }
    for old_activity in old_activities:
        stats["total"] += 1
        new_activity = new_activities.get(
            (
                old_activity.user_id,
                old_activity.action,
                old_activity.actionable_id,
                old_activity.actionable_type,
                old_activity.created_at,
            )
        )
        if new_activity is None:
            if old_activity.actionable_type == "Budget::Investment":
                actionable_id = id_maps["budget_investments"].get(
                    old_activity.actionable_id
                )
                if actionable_id is None:
                    print(
                        f"Missing budget investment. Old id: {old_activity.actionable_id}"
                    )
                    continue
            elif old_activity.actionable_type == "Newsletter":
                actionable_id = id_maps["newsletters"].get(old_activity.actionable_id)
                if actionable_id is None:
                    print(f"Missing newsletter. Old id: {old_activity.actionable_id}")
                    continue
            else:
                print(f"Actividad en tipo no soportado: {old_activity.actionable_type}")
                continue
            new_activity = NewActivity(
                user_id=id_maps["users"][old_activity.user_id],
                action=old_activity.action,
                actionable_type=old_activity.actionable_type,
                actionable_id=actionable_id,
                created_at=old_activity.created_at,
            )

        new_activity.updated_at = old_activity.updated_at

        await new_activity.save()
        stats["migrated"] += 1
        id_maps["activities"][str(old_activity.id)] = new_activity.id

    migration_stats["activities"] = stats
