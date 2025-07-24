from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewBudgetHeading(Model):
    class Meta:
        table = "budget_headings"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "group_id"
    group_id = fields.IntField(null=True)
    # t.bigint "price"
    price = fields.BigIntField(null=True)
    # t.integer "population"
    population = fields.IntField(null=True)
    # t.string "slug"
    slug = fields.CharField(max_length=255, null=True)
    # t.boolean "allow_custom_content", default: false
    allow_custom_content = fields.BooleanField(default=False)
    # t.text "latitude"
    latitude = fields.TextField(default="")
    # t.text "longitude"
    longitude = fields.TextField(default="")
    # t.integer "geozone_id"
    geozone_id = fields.IntField(null=True)
    # t.integer "max_ballot_lines", default: 1
    max_ballot_lines = fields.IntField(default=1)
    # t.datetime "created_at", precision: nil
    created_at = NaiveDatetimeField(null=True)
    # t.datetime "updated_at", precision: nil
    updated_at = NaiveDatetimeField(null=True)
    # t.integer "required_support"
    # TODO: required_support = fields.IntField(null=True)


"""
CREATE TABLE public.budget_headings (
    id integer NOT NULL,
    group_id integer,
    price bigint,
    population integer,
    slug character varying,
    allow_custom_content boolean DEFAULT false,
    latitude text,
    longitude text,
    geozone_id integer,
    max_ballot_lines integer DEFAULT 1,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    required_support integer
);
"""


class NewBudgetHeadingTranslation(Model):
    class Meta:
        table = "budget_heading_translations"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "budget_heading_id", null: false
    budget_heading_id = fields.IntField()
    # t.string "locale", null: false
    locale = fields.CharField(max_length=255)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.string "name"
    name = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.budget_heading_translations (
    id integer NOT NULL,
    budget_heading_id integer NOT NULL,
    locale character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    name character varying
);
"""
