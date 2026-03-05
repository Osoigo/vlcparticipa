from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldNotification(Model):
    class Meta:
        table = "notifications"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)
    # t.integer "notifiable_id"
    notifiable_id = fields.IntField(null=True)
    # t.string "notifiable_type"
    notifiable_type = fields.CharField(max_length=255, null=True)
    # t.integer "counter", default: 1
    counter = fields.IntField(null=True, default=1)
    # t.datetime "emailed_at"
    emailed_at = NaiveDatetimeField(null=True)
    # t.datetime "read_at"
    read_at = NaiveDatetimeField(null=True)


"""
CREATE TABLE public.notifications (
    id integer NOT NULL,
    user_id integer,
    notifiable_id integer,
    notifiable_type character varying,
    counter integer DEFAULT 1,
    emailed_at timestamp without time zone,
    read_at timestamp without time zone
);
"""
