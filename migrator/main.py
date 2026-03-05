import json
import traceback
from pathlib import Path
from pprint import pp
from tortoise import Tortoise, run_async

from . import settings
from . import migrators


async def run():
    await Tortoise.init(
        {
            "connections": {
                "old": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": settings.OLD_DATABASE_HOST,
                        "port": settings.OLD_DATABASE_PORT,
                        "user": settings.OLD_DATABASE_USER,
                        "password": settings.OLD_DATABASE_PASSWORD,
                        "database": settings.OLD_DATABASE_NAME,
                    },
                },
                "new": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": settings.NEW_DATABASE_HOST,
                        "port": settings.NEW_DATABASE_PORT,
                        "user": settings.NEW_DATABASE_USER,
                        "password": settings.NEW_DATABASE_PASSWORD,
                        "database": settings.NEW_DATABASE_NAME,
                    },
                },
            },
            "apps": {
                "old": {
                    "models": ["migrator.models.old_models"],
                    "default_connection": "old",
                },
                "new": {
                    "models": ["migrator.models.new_models"],
                    "default_connection": "new",
                },
            },
        }
    )

    id_maps_file = Path("id_maps.json")
    if id_maps_file.exists():
        with id_maps_file.open() as f:
            id_maps = json.load(f)
    else:
        id_maps = {}
    stats_file = Path("stats.json")
    if stats_file.exists():
        with stats_file.open() as f:
            stats = json.load(f)
    else:
        stats = {}
    try:
        print("Migrate geozones")
        await migrators.geozones.migrate(id_maps, stats)
        print("Migrate newsletters")
        await migrators.newsletters.migrate(id_maps, stats)
        print("Migrate users")
        await migrators.users.migrate(id_maps, stats)
        print("Migrate managers")
        await migrators.managers.migrate(id_maps, stats)
        print("Migrate valuators")
        await migrators.valuators.migrate(id_maps, stats)
        print("Migrate administrators")
        await migrators.administrators.migrate(id_maps, stats)
        print("Migrate communities")
        await migrators.communities.migrate(id_maps, stats)
        print("Migrate budgets")
        await migrators.budgets.migrate(id_maps, stats)
        print("Migrate budget_phases")
        await migrators.budget_phases.migrate(id_maps, stats)
        print("Migrate budget_groups")
        await migrators.budget_groups.migrate(id_maps, stats)
        print("Migrate budget_headings")
        await migrators.budget_headings.migrate(id_maps, stats)
        print("Migrate budget_investments")
        await migrators.budget_investments.migrate(id_maps, stats)
        print("Migrate budget_valuator_assignments")
        await migrators.budget_valuator_assignments.migrate(id_maps, stats)
        print("Migrate budget_ballots")
        await migrators.budget_ballots.migrate(id_maps, stats)
        print("Migrate budget_investment_milestones")
        await migrators.budget_investment_milestones.migrate(id_maps, stats)
        print("Migrate budget_reclassified_votes")
        await migrators.budget_reclassified_votes.migrate(id_maps, stats)
        print("Migrate tags")
        await migrators.tags.migrate(id_maps, stats)
        print("Migrate votes")
        await migrators.votes.migrate(id_maps, stats)
        print("Migrate images")
        await migrators.images.migrate(id_maps, stats)
        print("Migrate documents")
        await migrators.documents.migrate(id_maps, stats)
        print("Migrate map_locations")
        await migrators.map_locations.migrate(id_maps, stats)
        print("Migrate comments")
        await migrators.comments.migrate(id_maps, stats)
        print("Migrate activities")
        await migrators.activities.migrate(id_maps, stats)
        print("Migrate visits")
        await migrators.visits.migrate(id_maps, stats)
        print("Migrate delayed_jobs")
        await migrators.delayed_jobs.migrate(id_maps, stats)
        print("Migrate failed_census_calls")
        await migrators.failed_census_calls.migrate(id_maps, stats)
        print("Migrate i18n_contents")
        await migrators.i18n_contents.migrate(id_maps, stats)
        print("Migrate notifications")
        await migrators.notifications.migrate(id_maps, stats)
        print("Migrate locks")
        await migrators.locks.migrate(id_maps, stats)
        print("Migrate widget_feeds")
        await migrators.widget_feeds.migrate(id_maps, stats)
    except Exception as e:
        print(e)
        traceback.print_exc()

    with id_maps_file.open("w") as f:
        json.dump(indent=2, fp=f, obj=id_maps)

    with stats_file.open("w") as f:
        json.dump(indent=2, fp=f, obj=stats)

    await Tortoise.close_connections()
    pp(stats)


if __name__ == "__main__":
    run_async(run())
