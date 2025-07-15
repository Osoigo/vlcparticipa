from tortoise.models import Model
from tortoise import fields


class OldMapLocation(Model):
    class Meta:
        table = "map_locations"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.float "latitude"
    latitude = fields.FloatField(null=True)
    # t.float "longitude"
    longitude = fields.FloatField(null=True)
    # t.integer "zoom"
    zoom = fields.IntField(null=True)
    # t.integer "proposal_id"
    proposal_id = fields.IntField(null=True)
    # t.integer "investment_id"
    investment_id = fields.IntField(null=True)


"""
CREATE TABLE public.map_locations (
    id integer NOT NULL,
    latitude double precision,
    longitude double precision,
    zoom integer,
    proposal_id integer,
    investment_id integer
);
"""
