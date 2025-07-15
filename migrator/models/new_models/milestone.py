from tortoise import fields
from tortoise.models import Model

from ...custom_fields import NaiveDatetimeField


class NewMilestoneStatus(Model):
    class Meta:
        table = "milestone_statuses"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string "name"
    name = fields.CharField(max_length=255, null=True)
    # t.text "description"
    description = fields.TextField(null=True)
    # t.datetime "hidden_at", precision: nil
    hidden_at = NaiveDatetimeField(null=True)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.milestone_statuses (
    id integer NOT NULL,
    name character varying,
    description text,
    hidden_at timestamp without time zone,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
"""


class NewMilestone(Model):
    class Meta:
        table = "milestones"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string "milestoneable_type"
    milestoneable_type = fields.CharField(max_length=255, null=True)
    # t.integer "milestoneable_id"
    milestoneable_id = fields.IntField(null=True)
    # t.datetime "publication_date", precision: nil
    publication_date = NaiveDatetimeField(null=True)
    # t.integer "status_id"
    status_id = fields.IntField(null=True)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()


"""
CREATE TABLE public.milestones (
    id integer NOT NULL,
    milestoneable_type character varying,
    milestoneable_id integer,
    publication_date timestamp without time zone,
    status_id integer,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
"""


class NewMilestoneTranslation(Model):
    class Meta:
        table = "milestone_translations"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "milestone_id", null: false
    milestone_id = fields.IntField(null=False)
    # t.string "locale", null: false
    locale = fields.CharField(max_length=255)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.string "title"
    title = fields.CharField(max_length=255, null=True)
    # t.text "description"
    description = fields.TextField(null=True)


"""
CREATE TABLE public.milestone_translations (
    id integer NOT NULL,
    milestone_id integer NOT NULL,
    locale character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    title character varying,
    description text
);
"""
