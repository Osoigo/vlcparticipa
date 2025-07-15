from tortoise.models import Model
from tortoise import fields


class NewAdministrator(Model):
    class Meta:
        table = "administrators"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)
    # t.string "description"
    description = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.administrators (
    id integer NOT NULL,
    user_id integer,
    description character varying
);
"""
