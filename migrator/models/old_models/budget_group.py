from tortoise.models import Model
from tortoise import fields


class OldBudgetGroup(Model):
    class Meta:
        table = "budget_groups"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer "budget_id"
    budget_id = fields.IntField(null=True)
    # t.string  "name", limit: 50
    name = fields.CharField(max_length=255, null=True)
    # t.string  "slug"
    slug = fields.CharField(max_length=255, null=True)
    # t.integer "max_votable_headings", default: 1
    max_votable_headings = fields.IntField(default=1)


"""
CREATE TABLE public.budget_groups (
    id integer NOT NULL,
    budget_id integer,
    name character varying(50),
    slug character varying,
    max_votable_headings integer DEFAULT 1
);
"""
