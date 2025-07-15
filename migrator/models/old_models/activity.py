from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldActivity(Model):
    class Meta:
        table = "activities"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer  "user_id"
    user_id = fields.IntField(null=True)
    # t.string   "action"
    action = fields.CharField(max_length=255, null=True)
    # t.integer  "actionable_id"
    actionable_id = fields.IntField(null=True)
    # t.string   "actionable_type"
    actionable_type = fields.CharField(max_length=255, null=True)
    # t.datetime "created_at"
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at"
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.activities (
    id integer NOT NULL,
    user_id integer,
    action character varying,
    actionable_id integer,
    actionable_type character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);
"""
