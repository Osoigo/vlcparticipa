from ..models.new_models.map_location import NewMapLocation
from ..models.old_models.map_location import OldMapLocation


async def migrate(id_maps):
    id_maps["map_locations"] = {}
    old_map_locations = await OldMapLocation.all()
    new_map_locations = {m.investment_id: m for m in await NewMapLocation.all()}
    for old_map_location in old_map_locations:
        if old_map_location.proposal_id is not None:
            continue  # En producción solo hay investment_ids
        new_map_location = new_map_locations.get(old_map_location.investment_id)
        if new_map_location is None:
            new_map_location = NewMapLocation(
                investment_id=id_maps["budget_investments"][
                    old_map_location.investment_id
                ]
            )
        new_map_location.latitude = old_map_location.latitude
        new_map_location.longitude = old_map_location.longitude
        new_map_location.zoom = old_map_location.zoom

        await new_map_location.save()

        id_maps["map_locations"][old_map_location.id] = new_map_location.id
