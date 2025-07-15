from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldNewsletter(Model):
    class Meta:
        table = "newsletters"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.string   "subject"
    subject = fields.CharField(max_length=255, null=True)
    # t.string   "segment_recipient", null: false
    segment_recipient = fields.CharField(max_length=255)
    # t.string   "from"
    _from = fields.CharField(max_length=255, null=True, source_field="from")
    # t.text     "body"
    body = fields.TextField(null=True)
    # t.date     "sent_at"
    sent_at = NaiveDatetimeField(null=True)
    # t.datetime "created_at",        null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at",        null: false
    updated_at = NaiveDatetimeField()
    # t.datetime "hidden_at"
    hidden_at = NaiveDatetimeField(null=True)


"""
CREATE TABLE public.newsletters (
    id integer NOT NULL,
    subject character varying,
    segment_recipient character varying NOT NULL,
    "from" character varying,
    body text,
    sent_at date,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    hidden_at timestamp without time zone
);
"""
