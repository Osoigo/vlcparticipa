from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldComment(Model):
    class Meta:
        table = "comments"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer "commentable_id"
    commentable_id = fields.IntField(null=True)
    # t.string "commentable_type"
    commentable_type = fields.CharField(max_length=255, null=True)
    # t.text "body"
    body = fields.TextField(null=True)
    # t.string "subject"
    subject = fields.CharField(max_length=255, null=True)
    # t.integer "user_id", null: false
    user_id = fields.IntField()
    # t.datetime "created_at"
    created_at = NaiveDatetimeField(null=True)
    # t.datetime "updated_at"
    updated_at = NaiveDatetimeField(null=True)
    # t.datetime "hidden_at"
    hidden_at = NaiveDatetimeField(null=True)
    # t.integer "flags_count", default: 0
    flags_count = fields.IntField(default=0)
    # t.datetime "ignored_flag_at"
    ignored_flag_at = NaiveDatetimeField(null=True)
    # t.integer "moderator_id"
    moderator_id = fields.IntField(null=True)
    # t.integer "administrator_id"
    administrator_id = fields.IntField(null=True)
    # t.integer "cached_votes_total", default: 0
    cached_votes_total = fields.IntField(default=0)
    # t.integer "cached_votes_up", default: 0
    cached_votes_up = fields.IntField(default=0)
    # t.integer "cached_votes_down", default: 0
    cached_votes_down = fields.IntField(default=0)
    # t.datetime "confirmed_hide_at"
    confirmed_hide_at = NaiveDatetimeField(null=True)
    # t.string "ancestry"
    ancestry = fields.CharField(max_length=255, null=True)
    # t.integer "confidence_score", default: 0, null: false
    confidence_score = fields.IntField(default=0)
    # t.boolean "valuation", default: false
    valuation = fields.BooleanField(default=False)


"""
CREATE TABLE public.comments (
    id integer NOT NULL,
    commentable_id integer,
    commentable_type character varying,
    body text,
    subject character varying,
    user_id integer NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    hidden_at timestamp without time zone,
    flags_count integer DEFAULT 0,
    ignored_flag_at timestamp without time zone,
    moderator_id integer,
    administrator_id integer,
    cached_votes_total integer DEFAULT 0,
    cached_votes_up integer DEFAULT 0,
    cached_votes_down integer DEFAULT 0,
    confirmed_hide_at timestamp without time zone,
    ancestry character varying,
    confidence_score integer DEFAULT 0 NOT NULL,
    valuation boolean DEFAULT false
);
"""
