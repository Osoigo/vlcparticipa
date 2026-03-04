from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewDelayedJob(Model):
    class Meta:
        table = "delayed_jobs"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "priority", default: 0, null: false
    priority = fields.IntField(default=0)
    # t.integer "attempts", default: 0, null: false
    attempts = fields.IntField(default=0)
    # t.text "handler", null: false
    handler = fields.TextField()
    # t.text "last_error"
    last_error = fields.TextField()
    # t.datetime "run_at", precision: nil
    run_at = NaiveDatetimeField()
    # t.datetime "locked_at", precision: nil
    locked_at = NaiveDatetimeField()
    # t.datetime "failed_at", precision: nil
    failed_at = NaiveDatetimeField()
    # t.string "locked_by"
    locked_by = fields.CharField(max_length=255, null=True)
    # t.string "queue"
    queue = fields.CharField(max_length=255, null=True)
    # t.datetime "created_at", precision: nil
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil
    updated_at = NaiveDatetimeField()
    # t.string "tenant"
    tenant = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.delayed_jobs (
    id integer NOT NULL,
    priority integer DEFAULT 0 NOT NULL,
    attempts integer DEFAULT 0 NOT NULL,
    handler text NOT NULL,
    last_error text,
    run_at timestamp without time zone,
    locked_at timestamp without time zone,
    failed_at timestamp without time zone,
    locked_by character varying,
    queue character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    tenant character varying
);
"""
