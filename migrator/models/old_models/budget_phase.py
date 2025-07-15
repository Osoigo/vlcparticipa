from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldBudgetPhase(Model):
    class Meta:
        table = "budget_phases"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer  "budget_id"
    budget_id = fields.IntField(null=True)
    # t.integer  "next_phase_id"
    next_phase_id = fields.IntField(null=True)
    # t.string   "kind", null: false
    kind = fields.CharField(max_length=255)
    # t.text     "summary"
    summary = fields.TextField(null=True)
    # t.text     "description"
    description = fields.TextField(null=True)
    # t.datetime "starts_at"
    starts_at = NaiveDatetimeField(null=True)
    # t.datetime "ends_at"
    ends_at = NaiveDatetimeField(null=True)
    # t.boolean  "enabled",       default: true
    enabled = fields.BooleanField(default=True)


"""
CREATE TABLE public.budget_phases (
    id integer NOT NULL,
    budget_id integer,
    next_phase_id integer,
    kind character varying NOT NULL,
    summary text,
    description text,
    starts_at timestamp without time zone,
    ends_at timestamp without time zone,
    enabled boolean DEFAULT true
);
"""
