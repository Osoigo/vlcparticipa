from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewWidgetFeed(Model):
    class Meta:
        table = "widget_feeds"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string "kind"
    kind = fields.CharField(max_length=255, null=True)
    # t.integer "limit", default: 3
    limit = fields.IntField(null=True, default=3)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.widget_feeds (
    id integer NOT NULL,
    kind character varying,
    "limit" integer DEFAULT 3,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
"""
