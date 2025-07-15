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

    id_maps = {}
    print("Migrate geozones")
    await migrators.geozones.migrate(id_maps)
    print("Migrate users")
    await migrators.users.migrate(id_maps)
    print("Migrate managers")
    await migrators.managers.migrate(id_maps)
    print("Migrate valuators")
    await migrators.valuators.migrate(id_maps)
    print("Migrate administrators")
    await migrators.administrators.migrate(id_maps)
    print("Migrate communities")
    await migrators.communities.migrate(id_maps)
    print("Migrate budgets")
    await migrators.budgets.migrate(id_maps)
    print("Migrate budget_phases")
    await migrators.budget_phases.migrate(id_maps)
    print("Migrate budget_groups")
    await migrators.budget_groups.migrate(id_maps)
    print("Migrate budget_headings")
    await migrators.budget_headings.migrate(id_maps)
    print("Migrate budget_investments")
    await migrators.budget_investments.migrate(id_maps)
    print("Migrate budget_valuator_assignments")
    await migrators.budget_valuator_assignments.migrate(id_maps)
    print("Migrate budget_ballots")
    await migrators.budget_ballots.migrate(id_maps)
    print("Migrate budget_investment_milestones")
    await migrators.budget_investment_milestones.migrate(id_maps)
    print("Migrate tags")
    await migrators.tags.migrate(id_maps)
    print("Migrate votes")
    await migrators.votes.migrate(id_maps)
    print("Migrate images")
    await migrators.images.migrate(id_maps)
    print("Migrate map_locations")
    await migrators.map_locations.migrate(id_maps)
    print("Migrate comments")
    await migrators.comments.migrate(id_maps)
    print("Migrate newsletters")
    await migrators.newsletters.migrate(id_maps)
    print("Migrate activities")
    await migrators.activities.migrate(id_maps)
    print("Migrate visits")
    await migrators.visits.migrate(id_maps)

    pp(id_maps)

    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(run())
