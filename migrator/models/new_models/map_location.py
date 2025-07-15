from tortoise.models import Model
from tortoise import fields


class NewMapLocation(Model):
    class Meta:
        table = "map_locations"
        app = "new"

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

    # t.float "latitude"
    # t.float "longitude"
    # t.integer "zoom"
    # t.integer "proposal_id"
    # t.integer "investment_id"


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
