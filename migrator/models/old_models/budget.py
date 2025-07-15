from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldBudget(Model):
    class Meta:
        table = "budgets"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.string "name", limit: 80
    name = fields.CharField(max_length=80, null=True)
    # t.string "currency_symbol", limit: 10
    currency_symbol = fields.CharField(max_length=10, null=True)
    # t.string "phase", limit: 40, default: "accepting"
    phase = fields.CharField(max_length=40, default="accepting")
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
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
    # t.string "vote_types"
    vote_types = fields.CharField(max_length=255, null=True)
    # t.text "description_waiting"
    description_waiting = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.budgets (
    id integer NOT NULL,
    name character varying(80),
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
    vote_types character varying,
    description_waiting text
);
"""
