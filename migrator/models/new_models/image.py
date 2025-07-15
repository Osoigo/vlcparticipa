from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewImage(Model):
    class Meta:
        table = "images"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer  "imageable_id"
    imageable_id = fields.IntField(null=True)
    # t.string   "imageable_type"
    imageable_type = fields.CharField(max_length=255, null=True)
    # t.string   "title", limit: 80
    title = fields.CharField(max_length=80, null=True)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()
    # t.integer  "user_id"
    user_id = fields.IntField(null=True)


"""
CREATE TABLE public.images (
    id integer NOT NULL,
    imageable_type character varying,
    imageable_id integer,
    title character varying(80),
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    user_id integer
);
"""
