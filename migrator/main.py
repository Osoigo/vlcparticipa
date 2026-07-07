import datetime
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

    STEPS = (
        ("Migrate geozones", migrators.geozones),
        ("Migrate newsletters", migrators.newsletters),
        ("Migrate users", migrators.users),
        ("Migrate managers", migrators.managers),
        ("Migrate valuators", migrators.valuators),
        ("Migrate administrators", migrators.administrators),
        ("Migrate communities", migrators.communities),
        ("Migrate budgets", migrators.budgets),
        ("Migrate budget_phases", migrators.budget_phases),
        ("Migrate budget_groups", migrators.budget_groups),
        ("Migrate budget_headings", migrators.budget_headings),
        ("Migrate budget_investments", migrators.budget_investments),
        ("Migrate budget_valuator_assignments", migrators.budget_valuator_assignments),
        ("Migrate budget_ballots", migrators.budget_ballots),
        (
            "Migrate budget_investment_milestones",
            migrators.budget_investment_milestones,
        ),
        ("Migrate budget_reclassified_votes", migrators.budget_reclassified_votes),
        ("Migrate tags", migrators.tags),
        ("Migrate votes", migrators.votes),
        ("Migrate images", migrators.images),
        ("Migrate documents", migrators.documents),
        ("Migrate map_locations", migrators.map_locations),
        ("Migrate comments", migrators.comments),
        ("Migrate delayed_jobs", migrators.delayed_jobs),
        ("Migrate failed_census_calls", migrators.failed_census_calls),
        ("Migrate i18n_contents", migrators.i18n_contents),
        ("Migrate notifications", migrators.notifications),
        ("Migrate locks", migrators.locks),
        ("Migrate widget_feeds", migrators.widget_feeds),
        ("Migrate activities", migrators.activities),
        ("Migrate visits", migrators.visits),
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
        for step_name, step in STEPS:
            print(f"{datetime.datetime.now().strftime('%H:%M:%S')} - {step_name}")
            await step.migrate(id_maps, stats)

            # write id_maps.json and stats.json every step, as the program can die for excesive memory usage
            with id_maps_file.open("w") as f:
                json.dump(indent=2, fp=f, obj=id_maps)
            with stats_file.open("w") as f:
                json.dump(indent=2, fp=f, obj=stats)
    except Exception as e:
        print(e)
        traceback.print_exc()

    await Tortoise.close_connections()
    pp(stats)


if __name__ == "__main__":
    run_async(run())
