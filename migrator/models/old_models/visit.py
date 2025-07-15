from tortoise.models import Model
from tortoise import fields

from ...custom_fields import DecimalField, NaiveDatetimeField


class OldVisit(Model):
    class Meta:
        table = "visits"
        app = "old"

    id = fields.UUIDField(primary_key=True)
    # t.uuid     "visitor_id"
    visitor_id = fields.UUIDField(null=True)
    # t.string   "ip"
    ip = fields.CharField(max_length=255, null=True)
    # t.text     "user_agent"
    user_agent = fields.TextField(null=True)
    # t.text     "referrer"
    referrer = fields.TextField(null=True)
    # t.text     "landing_page"
    landing_page = fields.TextField(null=True)
    # t.integer  "user_id"
    user_id = fields.IntField(null=True)
    # t.string   "referring_domain"
    referring_domain = fields.CharField(max_length=255, null=True)
    # t.string   "search_keyword"
    search_keyword = fields.CharField(max_length=255, null=True)
    # t.string   "browser"
    browser = fields.CharField(max_length=255, null=True)
    # t.string   "os"
    os = fields.CharField(max_length=255, null=True)
    # t.string   "device_type"
    device_type = fields.CharField(max_length=255, null=True)
    # t.integer  "screen_height"
    screen_height = fields.IntField(null=True)
    # t.integer  "screen_width"
    screen_width = fields.IntField(null=True)
    # t.string   "country"
    country = fields.CharField(max_length=255, null=True)
    # t.string   "region"
    region = fields.CharField(max_length=255, null=True)
    # t.string   "city"
    city = fields.CharField(max_length=255, null=True)
    # t.string   "postal_code"
    postal_code = fields.CharField(max_length=255, null=True)
    # t.decimal  "latitude"
    latitude = DecimalField(null=True)
    # t.decimal  "longitude"
    longitude = DecimalField(null=True)
    # t.string   "utm_source"
    utm_source = fields.CharField(max_length=255, null=True)
    # t.string   "utm_medium"
    utm_medium = fields.CharField(max_length=255, null=True)
    # t.string   "utm_term"
    utm_term = fields.CharField(max_length=255, null=True)
    # t.string   "utm_content"
    utm_content = fields.CharField(max_length=255, null=True)
    # t.string   "utm_campaign"
    utm_campaign = fields.CharField(max_length=255, null=True)
    # t.datetime "started_at"
    started_at = NaiveDatetimeField()


"""
CREATE TABLE public.visits (
    id uuid NOT NULL,
    visitor_id uuid,
    ip character varying,
    user_agent text,
    referrer text,
    landing_page text,
    user_id integer,
    referring_domain character varying,
    search_keyword character varying,
    browser character varying,
    os character varying,
    device_type character varying,
    screen_height integer,
    screen_width integer,
    country character varying,
    region character varying,
    city character varying,
    postal_code character varying,
    latitude numeric,
    longitude numeric,
    utm_source character varying,
    utm_medium character varying,
    utm_term character varying,
    utm_content character varying,
    utm_campaign character varying,
    started_at timestamp without time zone
);
"""
