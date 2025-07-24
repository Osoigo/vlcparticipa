from ..models.new_models.community import NewCommunity
from ..models.old_models.community import OldCommunity


async def migrate(id_maps, migration_stats):
    id_maps["communities"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_communities = await OldCommunity.all()
    new_communities = {
        (c.created_at, c.updated_at): c for c in await NewCommunity.all()
    }
    for old_community in old_communities:
        stats["total"] += 1
        new_community = new_communities.get(
            (old_community.created_at, old_community.updated_at)
        )
        if new_community is None:
            new_community = NewCommunity(
                created_at=old_community.created_at, updated_at=old_community.updated_at
            )
        await new_community.save()
        stats["migrated"] += 1
        id_maps["communities"][str(old_community.id)] = new_community.id

    migration_stats["communities"] = stats
