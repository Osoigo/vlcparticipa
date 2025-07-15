from tortoise.models import Model
from tortoise import fields


class NewValuator(Model):
    class Meta:
        table = "valuators"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)
    # t.string "description"
    description = fields.CharField(max_length=255, null=True)
    # t.integer "budget_investments_count", default: 0
    budget_investments_count = fields.IntField(default=0)
    # t.integer "valuator_group_id"
    valuator_group_id = fields.IntField(null=True)
    # t.boolean "can_comment", default: true
    can_comment = fields.BooleanField(default=True)
    # t.boolean "can_edit_dossier", default: true
    can_edit_dossier = fields.BooleanField(default=True)


"""
CREATE TABLE public.valuators (
    id integer NOT NULL,
    user_id integer,
    description character varying,
    budget_investments_count integer DEFAULT 0,
    valuator_group_id integer,
    can_comment boolean DEFAULT true,
    can_edit_dossier boolean DEFAULT true
);
"""
