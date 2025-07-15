from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldGeozone(Model):
    class Meta:
        table = "geozones"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.string   "name"
    name = fields.CharField(max_length=255, null=True)
    # t.string   "html_map_coordinates"
    html_map_coordinates = fields.CharField(max_length=500, null=True)
    # t.string   "external_code"
    external_code = fields.CharField(max_length=255, null=True)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()
    # t.string   "census_code"
    census_code = fields.CharField(max_length=255, null=True)
    # t.integer  "parent_id"
    parent_id = fields.IntField(null=True)


"""
CREATE TABLE public.geozones (
    id integer NOT NULL,
    name character varying,
    html_map_coordinates character varying,
    external_code character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    census_code character varying,
    parent_id integer
);
"""
