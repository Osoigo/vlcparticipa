from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewDocument(Model):
    class Meta:
        table = "documents"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string "title"
    title = fields.CharField(max_length=255, null=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)
    # t.string "documentable_type"
    documentable_type = fields.CharField(max_length=255, null=True)
    # t.integer "documentable_id"
    documentable_id = fields.IntField(null=True)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.boolean "admin", default: false
    admin = fields.BooleanField(default=False)


"""
CREATE TABLE public.documents (
    id integer NOT NULL,
    title character varying,
    user_id integer,
    documentable_type character varying,
    documentable_id integer,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    admin boolean DEFAULT false
);
"""
