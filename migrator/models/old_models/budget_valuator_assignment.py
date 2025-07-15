from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldBudgetValuatorAssignment(Model):
    class Meta:
        table = "budget_valuator_assignments"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer  "valuator_id"
    valuator_id = fields.IntField(null=True)
    # t.integer  "investment_id"
    investment_id = fields.IntField(null=True)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.budget_valuator_assignments (
    id integer NOT NULL,
    valuator_id integer,
    investment_id integer,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
"""
