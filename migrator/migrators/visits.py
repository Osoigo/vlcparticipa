from uuid import uuid4
from ..models.new_models.visit import NewVisit
from ..models.old_models.visit import OldVisit


async def migrate(id_maps, migration_stats):
    # missing in new:
    #   old_visit.search_keyword
    #
    # new fields:
    #   new_visit.visit_token
    #   new_visit.visitor_token
    id_maps["visits"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_visits = await OldVisit.all()
    new_visits = {(v.visitor_id, v.started_at): v for v in await NewVisit.all()}
    for old_visit in old_visits:
        new_visit = new_visits.get((old_visit.visitor_id, old_visit.started_at))
        if new_visit is None:
            new_visit = NewVisit(
                id=str(uuid4()),
                visitor_id=old_visit.visitor_id,
                started_at=old_visit.started_at,
            )

        new_visit.ip = old_visit.ip
        new_visit.user_agent = old_visit.user_agent
        new_visit.referrer = old_visit.referrer
        new_visit.landing_page = old_visit.landing_page
        if old_visit.user_id is not None:
            user_id = id_maps["users"].get(str(old_visit.user_id))
            if user_id is None:
                print(f"Missing user. Old id: {old_visit.user_id}")
            new_visit.user_id = user_id
        new_visit.referring_domain = old_visit.referring_domain
        new_visit.browser = old_visit.browser
        new_visit.os = old_visit.os
        new_visit.device_type = old_visit.device_type
        new_visit.screen_height = old_visit.screen_height
        new_visit.screen_width = old_visit.screen_width
        new_visit.country = old_visit.country
        new_visit.region = old_visit.region
        new_visit.city = old_visit.city
        new_visit.postal_code = old_visit.postal_code
        new_visit.country = old_visit.country
        new_visit.latitude = old_visit.latitude
        new_visit.longitude = old_visit.longitude
        new_visit.utm_source = old_visit.utm_source
        new_visit.utm_medium = old_visit.utm_medium
        new_visit.utm_term = old_visit.utm_term
        new_visit.utm_content = old_visit.utm_content
        new_visit.utm_campaign = old_visit.utm_campaign
        new_visit.started_at = old_visit.started_at

        await new_visit.save()
        stats["migrated"] += 1
        id_maps["visits"][str(old_visit.id)] = str(new_visit.id)

    migration_stats["visits"] = stats
