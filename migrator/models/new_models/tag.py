from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewTag(Model):
    class Meta:
        table = "tags"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string  "name", limit: 40
    name = fields.CharField(max_length=160, null=True)
    # t.integer "taggings_count", default: 0
    taggings_count = fields.IntField(default=0)
    # t.integer "debates_count", default: 0
    debates_count = fields.IntField(default=0)
    # t.integer "proposals_count", default: 0
    proposals_count = fields.IntField(default=0)
    # t.string  "kind"
    kind = fields.CharField(max_length=255, null=True)
    # t.integer "budget/investments_count", default: 0
    budget_investments_count = fields.IntField(
        default=0,
    )
    # t.integer "legislation/proposals_count", default: 0
    legislation_proposals_count = fields.IntField(
        default=0,
    )
    # t.integer "legislation/processes_count", default: 0
    legislation_processes_count = fields.IntField(
        default=0,
    )


"""
CREATE TABLE public.tags (
    id integer NOT NULL,
    name character varying(160),
    taggings_count integer DEFAULT 0,
    debates_count integer DEFAULT 0,
    proposals_count integer DEFAULT 0,
    kind character varying,
    budget_investments_count integer DEFAULT 0,
    legislation_proposals_count integer DEFAULT 0,
    legislation_processes_count integer DEFAULT 0
);
"""


class NewTaggings(Model):
    class Meta:
        table = "taggings"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer  "tag_id"
    tag_id = fields.IntField(null=True)
    # t.integer  "taggable_id"
    taggable_id = fields.IntField(null=True)
    # t.string   "taggable_type"
    taggable_type = fields.CharField(max_length=255, null=True)
    # t.integer  "tagger_id"
    tagger_id = fields.IntField(null=True)
    # t.string   "tagger_type"
    tagger_type = fields.CharField(max_length=255, null=True)
    # t.string   "context",       limit: 128
    context = fields.CharField(max_length=128, null=True)
    # t.datetime "created_at"
    created_at = NaiveDatetimeField(null=True)


"""
CREATE TABLE public.taggings (
    id integer NOT NULL,
    tag_id integer,
    taggable_id integer,
    taggable_type character varying,
    tagger_id integer,
    tagger_type character varying,
    context character varying(128),
    created_at timestamp without time zone
);
"""
