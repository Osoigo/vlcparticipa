from tortoise import fields
from tortoise.models import Model

from ...custom_fields import NaiveDatetimeField


class OldBudgetInvestmentStatus(Model):
    class Meta:
        table = "budget_investment_statuses"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.string   "name"
    name = fields.CharField(max_length=255, null=True)
    # t.text     "description"
    description = fields.TextField(null=True)
    # t.datetime "hidden_at"
    hidden_at = NaiveDatetimeField(null=True)
    # t.datetime "created_at",  null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at",  null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.budget_investment_statuses (
    id integer NOT NULL,
    name character varying,
    description text,
    hidden_at timestamp without time zone,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
"""


class OldBudgetInvestmentMilestone(Model):
    class Meta:
        table = "budget_investment_milestones"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer  "investment_id"
    investment_id = fields.IntField(null=True)
    # t.string   "title", limit: 80
    title = fields.CharField(max_length=80, null=True)
    # t.text     "description"
    description = fields.TextField(default="")
    # t.datetime "created_at",                  null: false
    created_at = NaiveDatetimeField(null=True)
    # t.datetime "updated_at",                  null: false
    updated_at = NaiveDatetimeField(null=True)
    # t.datetime "publication_date"
    publication_date = NaiveDatetimeField(null=True)
    # t.integer  "status_id"
    status_id = fields.IntField(null=True)


"""
CREATE TABLE public.budget_investment_milestones (
    id integer NOT NULL,
    investment_id integer,
    title character varying(80),
    description text,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    publication_date timestamp without time zone,
    status_id integer
);
"""


class OldBudgetInvestmentMilestoneTranslation(Model):
    class Meta:
        table = "budget_investment_milestone_translations"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer  "budget_investment_milestone_id", null: false
    budget_investment_milestone_id = fields.IntField()
    # t.string   "locale", null: false
    locale = fields.CharField(max_length=255)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()
    # t.string   "title"
    title = fields.CharField(max_length=255, null=True)
    # t.text     "description"
    description = fields.TextField(null=True)


"""
CREATE TABLE public.budget_investment_milestone_translations (
    id integer NOT NULL,
    budget_investment_milestone_id integer NOT NULL,
    locale character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    title character varying,
    description text
);
"""
