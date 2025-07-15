from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldVote(Model):
    class Meta:
        table = "votes"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer  "votable_id"
    votable_id = fields.IntField(null=True)
    # t.string   "votable_type"
    votable_type = fields.CharField(max_length=255, null=True)
    # t.integer  "voter_id"
    voter_id = fields.IntField(null=True)
    # t.string   "voter_type"
    voter_type = fields.CharField(max_length=255, null=True)
    # t.boolean  "vote_flag"
    vote_flag = fields.BooleanField(null=True)
    # t.string   "vote_scope"
    vote_scope = fields.CharField(max_length=255, null=True)
    # t.integer  "vote_weight"
    vote_weight = fields.IntField(null=True)
    # t.datetime "created_at"
    created_at = NaiveDatetimeField(null=True)
    # t.datetime "updated_at"
    updated_at = NaiveDatetimeField(null=True)
    # t.integer  "signature_id"
    signature_id = fields.IntField(null=True)
    # t.datetime "refunded_at"
    refunded_at = NaiveDatetimeField(null=True)


"""
CREATE TABLE public.votes (
    id integer NOT NULL,
    votable_id integer,
    votable_type character varying,
    voter_id integer,
    voter_type character varying,
    vote_flag boolean,
    vote_scope character varying,
    vote_weight integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    signature_id integer,
    refunded_at timestamp without time zone
);
"""
