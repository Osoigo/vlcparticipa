from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewReport(Model):
    class Meta:
        table = "reports"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.boolean "stats"
    stats = fields.BooleanField()
    # t.boolean "results"
    results = fields.BooleanField()
    # t.string "process_type"
    process_type = fields.CharField(max_length=255, null=True)
    # t.integer "process_id"
    process_id = fields.IntField()
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.boolean "advanced_stats"
    advanced_stats = fields.BooleanField()


"""
CREATE TABLE public.reports (
    id integer NOT NULL,
    stats boolean,
    results boolean,
    process_type character varying,
    process_id integer,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    advanced_stats boolean
);
"""
