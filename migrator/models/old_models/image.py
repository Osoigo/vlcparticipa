from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldImage(Model):
    class Meta:
        table = "images"
        app = "old"

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
    # t.string   "attachment_file_name"
    attachment_file_name = fields.CharField(max_length=255, null=True)
    # t.string   "attachment_content_type"
    attachment_content_type = fields.CharField(max_length=255, null=True)
    # t.integer  "attachment_file_size"
    attachment_file_size = fields.IntField(null=True)
    # t.datetime "attachment_updated_at"
    attachment_updated_at = NaiveDatetimeField(null=True)
    # t.integer  "user_id"
    user_id = fields.IntField(null=True)


"""
CREATE TABLE public.images (
    id integer NOT NULL,
    imageable_id integer,
    imageable_type character varying,
    title character varying(80),
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    attachment_file_name character varying,
    attachment_content_type character varying,
    attachment_file_size integer,
    attachment_updated_at timestamp without time zone,
    user_id integer
);
"""
