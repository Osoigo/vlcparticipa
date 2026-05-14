from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewBudgetBallot(Model):
    class Meta:
        table = "budget_ballots"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer  "user_id"
    user_id = fields.IntField(null=True)
    # t.integer  "budget_id"
    budget_id = fields.IntField(null=True)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()
    # t.integer "ballot_lines_count", default: 0
    ballot_lines_count = fields.IntField(default=0)
    # t.integer "ballot_negativelines_count", default: 0
    ballot_negativelines_count = fields.IntField(default=0)
    # t.boolean "physical", default: false
    physical = fields.BooleanField(default=False)
    # t.integer "poll_ballot_id"
    poll_ballot_id = fields.IntField(null=True)


"""
CREATE TABLE public.budget_ballots (
    id integer NOT NULL,
    user_id integer,
    budget_id integer,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    ballot_lines_count integer DEFAULT 0,
    ballot_negativelines_count integer DEFAULT 0,
    physical boolean DEFAULT false,
    poll_ballot_id integer
);
"""


class NewBudgetBallotLine(Model):
    class Meta:
        table = "budget_ballot_lines"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "ballot_id"
    ballot_id = fields.IntField(null=True)
    # t.integer "investment_id"
    investment_id = fields.IntField(null=True)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.integer "budget_id"
    budget_id = fields.IntField(null=True)
    # t.integer "group_id"
    group_id = fields.IntField(null=True)
    # t.integer "heading_id"
    heading_id = fields.IntField(null=True)


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


class NewBudgetBallotNegativeline(Model):
    class Meta:
        table = "budget_ballot_negativelines"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.bigint "ballot_id"
    ballot_id = fields.IntField(null=True)
    # t.bigint "budget_id"
    budget_id = fields.IntField(null=True)
    # t.bigint "group_id"
    group_id = fields.IntField(null=True)
    # t.bigint "heading_id"
    heading_id = fields.IntField(null=True)
    # t.bigint "investment_id"
    investment_id = fields.IntField(null=True)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.budget_ballot_negativelines (
    id bigint NOT NULL,
    ballot_id integer,
    budget_id integer,
    group_id integer,
    heading_id integer,
    investment_id integer,
    created_at timestamp(6) without time zone NOT NULL,
    updated_at timestamp(6) without time zone NOT NULL
);
"""
