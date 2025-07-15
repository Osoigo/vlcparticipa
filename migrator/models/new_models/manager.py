from tortoise.models import Model
from tortoise import fields


class NewManager(Model):
    class Meta:
        table = "managers"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)


"""
CREATE TABLE public.managers (
    id integer NOT NULL,
    user_id integer,
);
"""
