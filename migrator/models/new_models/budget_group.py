from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewBudgetGroup(Model):
    class Meta:
        table = "budget_groups"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "budget_id"
    budget_id = fields.IntField(null=True)
    # t.string "slug"
    slug = fields.CharField(max_length=255, null=True)
    # t.integer "max_votable_headings", default: 1
    max_votable_headings = fields.IntField(default=1)
    # t.datetime "created_at", precision: nil
    created_at = NaiveDatetimeField(null=True)
    # t.datetime "updated_at", precision: nil
    updated_at = NaiveDatetimeField(null=True)


"""
CREATE TABLE public.budget_groups (
    id integer NOT NULL,
    budget_id integer,
    slug character varying,
    max_votable_headings integer DEFAULT 1,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);
"""


class NewBudgetGroupTranslation(Model):
    class Meta:
        table = "budget_group_translations"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "budget_group_id", null: false
    budget_group_id = fields.IntField()
    # t.string "locale", null: false
    locale = fields.CharField(max_length=255)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.string "name"
    name = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.budget_group_translations (
    id integer NOT NULL,
    budget_group_id integer NOT NULL,
    locale character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    name character varying
);
"""
