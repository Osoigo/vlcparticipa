from tortoise import fields
from tortoise.models import Model

from ...custom_fields import NaiveDatetimeField, TSVectorField


class OldBudgetInvestment(Model):
    class Meta:
        table = "budget_investments"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer "author_id"
    author_id = fields.IntField(null=True)
    # t.integer "administrator_id"
    administrator_id = fields.IntField(null=True)
    # t.string "title"
    title = fields.CharField(max_length=255, null=True)
    # t.text "description"
    description = fields.TextField(null=True)
    # t.string "external_url"
    external_url = fields.CharField(max_length=255, null=True)
    # t.integer "price", limit: 8
    price = fields.BigIntField(null=True)
    # t.string "feasibility", limit: 15, default: "undecided"
    feasibility = fields.CharField(max_length=15, default="undecided")
    # t.text "price_explanation"
    price_explanation = fields.TextField(null=True)
    # t.text "unfeasibility_explanation"
    unfeasibility_explanation = fields.TextField(null=True)
    # t.boolean "valuation_finished", default: false
    valuation_finished = fields.BooleanField(default=False)
    # t.integer "valuator_assignments_count", default: 0
    valuator_assignments_count = fields.IntField(default=0)
    # t.integer "price_first_year", limit: 8
    price_first_year = fields.BigIntField(null=True)
    # t.string "duration"
    duration = fields.CharField(max_length=255, null=True)
    # t.datetime "hidden_at"
    hidden_at = NaiveDatetimeField(null=True)
    # t.integer "cached_votes_up", default: 0
    cached_votes_up = fields.IntField(default=0)
    # t.integer "comments_count", default: 0
    comments_count = fields.IntField(default=0)
    # t.integer "confidence_score", default: 0, null: false
    confidence_score = fields.IntField(default=0)
    # t.integer "physical_votes", default: 0
    physical_votes = fields.IntField(default=0)
    # t.tsvector "tsv"
    tsv = TSVectorField(null=True)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()
    # t.integer "heading_id"
    heading_id = fields.IntField(null=True)
    # t.string "responsible_name"
    responsible_name = fields.CharField(max_length=255, null=True)
    # t.integer "budget_id"
    budget_id = fields.IntField(null=True)
    # t.integer "group_id"
    group_id = fields.IntField(null=True)
    # t.boolean "selected", default: false
    selected = fields.BooleanField(default=False)
    # t.string "location"
    location = fields.CharField(max_length=255, null=True)
    # t.string "organization_name"
    organization_name = fields.CharField(max_length=255, null=True)
    # t.datetime "unfeasible_email_sent_at"
    unfeasible_email_sent_at = NaiveDatetimeField(null=True)
    # t.integer "ballot_lines_count", default: 0
    ballot_lines_count = fields.IntField(default=0)
    # t.integer "previous_heading_id"
    previous_heading_id = fields.IntField(null=True)
    # t.boolean "winner", default: false
    winner = fields.BooleanField(default=False)
    # t.boolean "incompatible", default: false
    incompatible = fields.BooleanField(default=False)
    # t.integer "community_id"
    community_id = fields.IntField(null=True)
    # t.boolean "visible_to_valuators", default: false
    visible_to_valuators = fields.BooleanField(default=False)
    # t.integer "valuator_group_assignments_count", default: 0
    valuator_group_assignments_count = fields.IntField(default=0)
    # t.datetime "confirmed_hide_at"
    confirmed_hide_at = NaiveDatetimeField(null=True)
    # t.datetime "ignored_flag_at"
    ignored_flag_at = NaiveDatetimeField(null=True)
    # t.integer "flags_count", default: 0
    flags_count = fields.IntField(default=0)
    # t.string "unidad"
    unidad = fields.CharField(max_length=255, null=True)
    # t.string "proposed_service"
    proposed_service = fields.CharField(max_length=255, null=True)
    # t.string "other_services"
    other_services = fields.CharField(max_length=255, null=True)
    # t.boolean "allows_phase"
    allows_phase = fields.BooleanField(null=True)
    # t.float "price_phase1"
    price_phase1 = fields.FloatField(null=True)
    # t.float "price_phase2"
    price_phase2 = fields.FloatField(null=True)
    # t.float "price_phase3"
    price_phase3 = fields.FloatField(null=True)
    # t.float "price_phase4"
    price_phase4 = fields.FloatField(null=True)
    # t.string "budget_implementation"
    budget_implementation = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.budget_investments (
    id integer NOT NULL,
    author_id integer,
    administrator_id integer,
    title character varying,
    description text,
    external_url character varying,
    price bigint,
    feasibility character varying(15) DEFAULT 'undecided'::character varying,
    price_explanation text,
    unfeasibility_explanation text,
    valuation_finished boolean DEFAULT false,
    valuator_assignments_count integer DEFAULT 0,
    price_first_year bigint,
    duration character varying,
    hidden_at timestamp without time zone,
    cached_votes_up integer DEFAULT 0,
    comments_count integer DEFAULT 0,
    confidence_score integer DEFAULT 0 NOT NULL,
    physical_votes integer DEFAULT 0,
    tsv tsvector,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    heading_id integer,
    responsible_name character varying,
    budget_id integer,
    group_id integer,
    selected boolean DEFAULT false,
    location character varying,
    organization_name character varying,
    unfeasible_email_sent_at timestamp without time zone,
    ballot_lines_count integer DEFAULT 0,
    previous_heading_id integer,
    winner boolean DEFAULT false,
    incompatible boolean DEFAULT false,
    community_id integer,
    visible_to_valuators boolean DEFAULT false,
    valuator_group_assignments_count integer DEFAULT 0,
    confirmed_hide_at timestamp without time zone,
    ignored_flag_at timestamp without time zone,
    flags_count integer DEFAULT 0,
    unidad character varying,
    proposed_service character varying,
    other_services character varying,
    allows_phase boolean,
    price_phase1 double precision,
    price_phase2 double precision,
    price_phase3 double precision,
    price_phase4 double precision,
    budget_implementation character varying
);
"""
