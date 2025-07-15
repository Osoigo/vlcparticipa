from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldCommunity(Model):
    class Meta:
        table = "communities"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.communities (
    id integer NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
"""
