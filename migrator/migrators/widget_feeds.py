from ..models.new_models.widget_feed import NewWidgetFeed
from ..models.old_models.widget_feed import OldWidgetFeed


async def migrate(id_maps, migration_stats):
    id_maps["widget_feeds"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_widget_feeds = await OldWidgetFeed.all()
    new_widget_feeds = {w.created_at: w for w in await NewWidgetFeed.all()}
    for old_widget_feed in old_widget_feeds:
        stats["total"] += 1
        new_widget_feed = new_widget_feeds.get(old_widget_feed.created_at)
        if new_widget_feed is None:
            new_widget_feed = NewWidgetFeed(created_at=old_widget_feed.created_at)

        new_widget_feed.kind = old_widget_feed.kind
        new_widget_feed.limit = old_widget_feed.limit
        new_widget_feed.updated_at = old_widget_feed.updated_at

        await new_widget_feed.save()
        stats["migrated"] += 1
        id_maps["widget_feeds"][str(old_widget_feed.id)] = new_widget_feed.id

    migration_stats["widget_feeds"] = stats
