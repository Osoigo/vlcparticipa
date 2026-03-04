from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldBudgetReclasifiedVote(Model):
    class Meta:
        table = "budget_reclassified_votes"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)
    # t.integer "investment_id"
    investment_id = fields.IntField(null=True)
    # t.string "reason"
    reason = fields.CharField(max_length=255)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.budget_reclassified_votes (
    id integer NOT NULL,
    user_id integer,
    investment_id integer,
    reason character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
"""
