from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldBudgetBallot(Model):
    class Meta:
        table = "budget_ballots"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer  "user_id"
    user_id = fields.IntField(null=True)
    # t.integer  "budget_id"
    budget_id = fields.IntField(null=True)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()
    # t.integer  "ballot_old"
    ballot_old = fields.IntField(null=True)


"""
CREATE TABLE public.budget_ballots (
    id integer NOT NULL,
    user_id integer,
    budget_id integer,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    ballot_old integer
);
"""


class OldBudgetBallotLine(Model):
    class Meta:
        table = "budget_ballot_lines"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer  "ballot_id"
    ballot_id = fields.IntField(null=True)
    # t.integer  "investment_id"
    investment_id = fields.IntField(null=True)
    # t.datetime "created_at",    null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at",    null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.budget_ballot_lines (
    id integer NOT NULL,
    ballot_id integer,
    investment_id integer,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    budget_id integer,
    group_id integer,
    heading_id integer
);
"""
