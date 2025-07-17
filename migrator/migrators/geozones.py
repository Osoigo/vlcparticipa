from ..models.new_models.geozone import NewGeozone
from ..models.old_models.geozone import OldGeozone


async def migrate(id_maps):
    # missing in new:
    #   old_geozone.parent_id  ('all' en todos los buckets de producción)
    #
    # new fields:
    #   new_geozone.geojson
    #   new_geozone.color
    id_maps["geozones"] = {}
    old_geozones = await OldGeozone.all()
    new_geozones = {g.name: g for g in await NewGeozone.all()}
    for old_geozone in old_geozones:
        new_geozone = new_geozones.get(old_geozone.name)
        if new_geozone is None:
            new_geozone = NewGeozone(name=old_geozone.name)

        new_geozone.html_map_coordinates = old_geozone.html_map_coordinates
        new_geozone.external_code = old_geozone.external_code
        new_geozone.created_at = old_geozone.created_at
        new_geozone.updated_at = old_geozone.updated_at
        new_geozone.census_code = old_geozone.census_code

        await new_geozone.save()

        id_maps["geozones"][str(old_geozone.id)] = new_geozone.id
