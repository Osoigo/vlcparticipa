from ..models.new_models.notification import NewNotification
from ..models.old_models.notification import OldNotification


async def migrate(id_maps, migration_stats):
    id_maps["notifications"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_notifications = await OldNotification.all()
    new_notifications = {
        (n.user_id, n.notifiable_type, n.notifiable_id, n.counter, n.read_at): n
        for n in await NewNotification.all()
    }
    for old_notification in old_notifications:
        stats["total"] += 1

        if old_notification.notifiable_type == "Budget::Investment":
            notifiable_id = id_maps["budget_investments"][
                str(old_notification.notifiable_id)
            ]
        elif old_notification.notifiable_type == "Comment":
            notifiable_id = id_maps["comments"][str(old_notification.notifiable_id)]
        else:
            raise ValueError(
                f"Unexpected notifiable_type: {old_notification.notifiable_type}"
            )

        user_id = id_maps["users"][str(old_notification.user_id)]

        new_notification = new_notifications.get(
            (
                user_id,
                old_notification.notifiable_type,
                notifiable_id,
                old_notification.counter,
                old_notification.read_at,
            )
        )
        if new_notification is None:
            new_notification = NewNotification(
                user_id=user_id,
                notifiable_id=notifiable_id,
                counter=old_notification.counter,
                notifiable_type=old_notification.notifiable_type,
                read_at=old_notification.read_at,
            )

        new_notification.emailed_at = old_notification.emailed_at

        await new_notification.save()
        stats["migrated"] += 1
        id_maps["notifications"][str(old_notification.id)] = new_notification.id

    migration_stats["notifications"] = stats
