from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewBudgetPhase(Model):
    class Meta:
        table = "budget_phases"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "budget_id"
    budget_id = fields.IntField(null=True)
    # t.integer "next_phase_id"
    next_phase_id = fields.IntField(null=True)
    # t.string "kind", null: false
    kind = fields.CharField(max_length=255)
    # t.datetime "starts_at", precision: nil
    starts_at = NaiveDatetimeField(null=True)
    # t.datetime "ends_at", precision: nil
    ends_at = NaiveDatetimeField(null=True)
    # t.boolean "enabled", default: true
    enabled = fields.BooleanField(default=True)


"""
CREATE TABLE public.budget_phases (
    id integer NOT NULL,
    budget_id integer,
    next_phase_id integer,
    kind character varying NOT NULL,
    starts_at timestamp without time zone,
    ends_at timestamp without time zone,
    enabled boolean DEFAULT true
);
"""


class NewBudgetPhaseTranslation(Model):
    class Meta:
        table = "budget_phase_translations"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "budget_phase_id", null: false
    budget_phase_id = fields.IntField(null=True)
    # t.string "locale", null: false
    locale = fields.CharField(max_length=255)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField(null=True)
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField(null=True)
    # t.text "description"
    description = fields.TextField(null=True)
    # t.text "summary"
    summary = fields.TextField(null=True)
    # t.string "name"
    name = fields.CharField(max_length=255, null=True)
    # t.string "main_link_text"
    main_link_text = fields.CharField(max_length=255, null=True)
    # t.string "main_link_url"
    main_link_url = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.budget_phase_translations (
    id integer NOT NULL,
    budget_phase_id integer NOT NULL,
    locale character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    description text,
    summary text,
    name character varying,
    main_link_text character varying,
    main_link_url character varying
);
"""
