from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewGeozone(Model):
    class Meta:
        table = "geozones"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string "name"
    name = fields.CharField(max_length=255, null=True)
    # t.string "html_map_coordinates"
    html_map_coordinates = fields.CharField(max_length=500, null=True)
    # t.string "external_code"
    external_code = fields.CharField(max_length=255, null=True)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.string "census_code"
    census_code = fields.CharField(max_length=255, null=True)
    # t.text "geojson"
    geojson = fields.TextField(null=True)
    # t.string "color"
    color = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.geozones (
    id integer NOT NULL,
    name character varying,
    html_map_coordinates character varying,
    external_code character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    census_code character varying,
    geojson text,
    color character varying
);
"""
