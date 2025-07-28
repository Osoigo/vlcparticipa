from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldDocument(Model):
    class Meta:
        table = "documents"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.string "title"
    title = fields.CharField(max_length=255, null=True)
    # t.string "attachment_file_name"
    attachment_file_name = fields.CharField(max_length=255, null=True)
    # t.string "attachment_content_type"
    attachment_content_type = fields.CharField(max_length=255, null=True)
    # t.integer "attachment_file_size"
    attachment_file_size = fields.IntField(null=True)
    # t.datetime "attachment_updated_at"
    attachment_updated_at = NaiveDatetimeField()
    # t.integer "user_id"
    user_id = fields.IntField(null=True)
    # t.string "documentable_type"
    documentable_type = fields.CharField(max_length=255, null=True)
    # t.integer  "documentable_id"
    documentable_id = fields.IntField(null=True)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.documents (
    id integer NOT NULL,
    title character varying,
    attachment_file_name character varying,
    attachment_content_type character varying,
    attachment_file_size integer,
    attachment_updated_at timestamp without time zone,
    user_id integer,
    documentable_type character varying,
    documentable_id integer,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
"""
