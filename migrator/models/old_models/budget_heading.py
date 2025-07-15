from tortoise.models import Model
from tortoise import fields


class OldBudgetHeading(Model):
    class Meta:
        table = "budget_headings"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer "group_id"
    group_id = fields.IntField(null=True)
    # t.string  "name", limit: 50
    name = fields.CharField(max_length=50, null=True)
    # t.integer "price",            limit: 8
    price = fields.BigIntField(null=True)
    # t.integer "population"
    population = fields.IntField(null=True)
    # t.string  "slug"
    slug = fields.CharField(max_length=255, null=True)
    # t.integer "required_support"
    required_support = fields.IntField(null=True)


"""
CREATE TABLE public.budget_headings (
    id integer NOT NULL,
    group_id integer,
    name character varying(50),
    price bigint,
    population integer,
    slug character varying,
    required_support integer
);
"""
