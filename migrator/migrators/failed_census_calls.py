from ..models.new_models.failed_census_call import NewFailedCensusCall
from ..models.old_models.failed_census_call import OldFailedCensusCall


async def migrate(id_maps, migration_stats):
    id_maps["failed_census_calls"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_failed_census_calls = await OldFailedCensusCall.all()
    new_failed_census_calls = {f.created_at: f for f in await NewFailedCensusCall.all()}
    for old_failed_census_call in old_failed_census_calls:
        stats["total"] += 1
        new_failed_census_call = new_failed_census_calls.get(
            old_failed_census_call.created_at
        )
        if new_failed_census_call is None:
            new_failed_census_call = NewFailedCensusCall(
                created_at=old_failed_census_call.created_at
            )

        new_failed_census_call.user_id = id_maps["users"][
            str(old_failed_census_call.user_id)
        ]
        new_failed_census_call.document_number = old_failed_census_call.document_number
        new_failed_census_call.document_type = old_failed_census_call.document_type
        new_failed_census_call.date_of_birth = old_failed_census_call.date_of_birth
        new_failed_census_call.postal_code = old_failed_census_call.postal_code
        new_failed_census_call.updated_at = old_failed_census_call.updated_at
        new_failed_census_call.district_code = old_failed_census_call.district_code
        # new_failed_census_call.poll_officer_id = None  # In the old web all values where empty
        new_failed_census_call.year_of_birth = old_failed_census_call.year_of_birth

        await new_failed_census_call.save()

        stats["migrated"] += 1
        id_maps["failed_census_calls"][str(old_failed_census_call.id)] = (
            new_failed_census_call.id
        )

    migration_stats["failed_census_calls"] = stats
