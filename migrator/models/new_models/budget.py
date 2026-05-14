from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewBudget(Model):
    class Meta:
        table = "budgets"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string "currency_symbol", limit: 10
    currency_symbol = fields.CharField(max_length=10, null=True)
    # t.string "phase", limit: 40, default: "accepting"
    phase = fields.CharField(max_length=40, default="accepting")
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.text "description_accepting"
    description_accepting = fields.TextField(default="")
    # t.text "description_reviewing"
    description_reviewing = fields.TextField(default="")
    # t.text "description_selecting"
    description_selecting = fields.TextField(default="")
    # t.text "description_valuating"
    description_valuating = fields.TextField(default="")
    # t.text "description_balloting"
    description_balloting = fields.TextField(default="")
    # t.text "description_reviewing_ballots"
    description_reviewing_ballots = fields.TextField(default="")
    # t.text "description_finished"
    description_finished = fields.TextField(default="")
    # t.string "slug"
    slug = fields.CharField(max_length=255, null=True)
    # t.text "description_drafting"
    description_drafting = fields.TextField(default="")
    # t.text "description_publishing_prices"
    description_publishing_prices = fields.TextField(default="")
    # t.text "description_informing"
    description_informing = fields.TextField(default="")
    # t.string "voting_style", default: "knapsack"
    voting_style = fields.CharField(max_length=255, default="knapsack")
    # t.boolean "published"
    published = fields.BooleanField(null=True)
    # t.boolean "hide_money", default: false
    hide_money = fields.BooleanField(default=False)
    # t.integer "negative_votes", default: 0
    negative_votes = fields.IntField(default=0)
    # t.float "negative_vote_value", default: 0.5
    negative_vote_value = fields.FloatField(default=0.5)


"""
CREATE TABLE public.budgets (
    id integer NOT NULL,
    currency_symbol character varying(10),
    phase character varying(40) DEFAULT 'accepting'::character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    description_accepting text,
    description_reviewing text,
    description_selecting text,
    description_valuating text,
    description_balloting text,
    description_reviewing_ballots text,
    description_finished text,
    slug character varying,
    description_drafting text,
    description_publishing_prices text,
    description_informing text,
    voting_style character varying DEFAULT 'knapsack'::character varying,
    published boolean,
    hide_money boolean DEFAULT false,
    negative_votes integer DEFAULT 0,
    negative_vote_value double precision DEFAULT 0.5
);
"""


class NewBudgetTranslation(Model):
    class Meta:
        table = "budget_translations"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "budget_id", null: false
    budget_id = fields.IntField()
    # t.string "locale", null: false
    locale = fields.CharField(max_length=255)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField(null=True)
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField(null=True)
    # t.string "name"
    name = fields.CharField(max_length=255, null=True)
    # t.string "main_link_text"
    main_link_text = fields.CharField(max_length=255, null=True)
    # t.string "main_link_url"
    main_link_url = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.budget_translations (
    id integer NOT NULL,
    budget_id integer NOT NULL,
    locale character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    name character varying,
    main_link_text character varying,
    main_link_url character varying
);
"""
