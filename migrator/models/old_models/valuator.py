from tortoise.models import Model
from tortoise import fields


class OldValuator(Model):
    class Meta:
        table = "valuators"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)
    # t.string "description"
    description = fields.CharField(max_length=255, null=True)
    # t.integer "spending_proposals_count", default: 0
    spending_proposals_count = fields.IntField(default=0)
    # t.integer "budget_investments_count", default: 0
    budget_investments_count = fields.IntField(default=0)
    # t.integer "valuator_group_id"
    valuator_group_id = fields.IntField(null=True)


"""
CREATE TABLE public.valuators (
    id integer NOT NULL,
    user_id integer,
    description character varying,
    spending_proposals_count integer DEFAULT 0,
    budget_investments_count integer DEFAULT 0,
    valuator_group_id integer
);
"""
