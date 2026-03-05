from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewLock(Model):
    class Meta:
        table = "locks"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)
    # t.integer "tries", default: 0
    tries = fields.IntField(null=True, default=0)
    # t.datetime "locked_until", precision: nil, default: "2000-01-01 01:01:01", null: false
    locked_until = NaiveDatetimeField(default="2000-01-01 01:01:01")
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.locks (
    id integer NOT NULL,
    user_id integer,
    tries integer DEFAULT 0,
    locked_until timestamp without time zone DEFAULT '2000-01-01 01:01:01'::timestamp without time zone NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
"""
