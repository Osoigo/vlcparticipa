from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewFailedCensusCall(Model):
    class Meta:
        table = "failed_census_calls"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.integer "user_id"
    user_id = fields.IntField(null=True)
    # t.string "document_number"
    document_number = fields.CharField(max_length=255, null=True)
    # t.string "document_type"
    document_type = fields.CharField(max_length=255, null=True)
    # t.date "date_of_birth"
    date_of_birth = fields.DateField(null=True)
    # t.string "postal_code"
    postal_code = fields.CharField(max_length=255, null=True)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.string "district_code"
    district_code = fields.CharField(max_length=255, null=True)
    # t.integer "poll_officer_id"
    poll_officer_id = fields.IntField(null=True)
    # t.integer "year_of_birth"
    year_of_birth = fields.IntField(null=True)


"""
CREATE TABLE public.failed_census_calls (
    id integer NOT NULL,
    user_id integer,
    document_number character varying,
    document_type character varying,
    date_of_birth date,
    postal_code character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    district_code character varying,
    poll_officer_id integer,
    year_of_birth integer
);
"""
