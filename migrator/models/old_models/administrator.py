from tortoise.models import Model
from tortoise import fields


class OldAdministrator(Model):
    class Meta:
        table = "administrators"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)


"""
CREATE TABLE public.administrators (
    id integer NOT NULL,
    user_id integer
);
"""
