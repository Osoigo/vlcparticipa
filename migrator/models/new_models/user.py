from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewUser(Model):
    class Meta:
        table = "users"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string "email", default: ""
    email = fields.CharField(max_length=255, unique=True, null=True)
    # t.string "encrypted_password", default: "", null: false
    encrypted_password = fields.CharField(max_length=255)
    # t.string "reset_password_token"
    reset_password_token = fields.CharField(max_length=255, null=True)
    # t.datetime "reset_password_sent_at", precision: nil
    reset_password_sent_at = NaiveDatetimeField(null=True)
    # t.datetime "remember_created_at", precision: nil
    remember_created_at = NaiveDatetimeField(null=True)
    # t.integer "sign_in_count", default: 0, null: false
    sign_in_count = fields.IntField(default=0)
    # t.datetime "current_sign_in_at", precision: nil
    current_sign_in_at = NaiveDatetimeField(null=True)
    # t.datetime "last_sign_in_at", precision: nil
    last_sign_in_at = NaiveDatetimeField(null=True)
    # t.string "current_sign_in_ip"
    current_sign_in_ip = fields.CharField(max_length=255, null=True)
    # t.string "last_sign_in_ip"
    last_sign_in_ip = fields.CharField(max_length=255, null=True)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", precision: nil, null: false
    updated_at = NaiveDatetimeField()
    # t.string "confirmation_token"
    confirmation_token = fields.CharField(max_length=255, null=True)
    # t.datetime "confirmed_at", precision: nil
    confirmed_at = NaiveDatetimeField(null=True)
    # t.datetime "confirmation_sent_at", precision: nil
    confirmation_sent_at = NaiveDatetimeField(null=True)
    # t.string "unconfirmed_email"
    unconfirmed_email = fields.CharField(max_length=255, null=True)
    # t.boolean "email_on_comment", default: false
    email_on_comment = fields.BooleanField(default=False)
    # t.boolean "email_on_comment_reply", default: false
    email_on_comment_reply = fields.BooleanField(default=False)
    # t.string "phone_number", limit: 30
    phone_number = fields.CharField(max_length=30, null=True)
    # t.string "official_position"
    official_position = fields.CharField(max_length=255, null=True)
    # t.integer "official_level", default: 0
    official_level = fields.IntField(default=0)
    # t.datetime "hidden_at", precision: nil
    hidden_at = NaiveDatetimeField(null=True)
    # t.string "sms_confirmation_code"
    sms_confirmation_code = fields.CharField(max_length=255, null=True)
    # t.string "username", limit: 60
    username = fields.CharField(max_length=60, null=True)
    # t.string "document_number"
    document_number = fields.CharField(max_length=255, null=True)
    # t.string "document_type"
    document_type = fields.CharField(max_length=255, null=True)
    # t.datetime "residence_verified_at", precision: nil
    residence_verified_at = NaiveDatetimeField(null=True)
    # t.string "email_verification_token"
    email_verification_token = fields.CharField(max_length=255, null=True)
    # t.datetime "verified_at", precision: nil
    verified_at = NaiveDatetimeField(null=True)
    # t.string "unconfirmed_phone"
    unconfirmed_phone = fields.CharField(max_length=255, null=True)
    # t.string "confirmed_phone"
    confirmed_phone = fields.CharField(max_length=255, null=True)
    # t.datetime "letter_requested_at", precision: nil
    letter_requested_at = NaiveDatetimeField(null=True)
    # t.datetime "confirmed_hide_at", precision: nil
    confirmed_hide_at = NaiveDatetimeField(null=True)
    # t.string "letter_verification_code"
    letter_verification_code = fields.CharField(max_length=255, null=True)
    # t.integer "failed_census_calls_count", default: 0
    failed_census_calls_count = fields.IntField(default=0)
    # t.datetime "level_two_verified_at", precision: nil
    level_two_verified_at = NaiveDatetimeField(null=True)
    # t.string "erase_reason"
    erase_reason = fields.CharField(max_length=255, null=True)
    # t.datetime "erased_at", precision: nil
    erased_at = NaiveDatetimeField(null=True)
    # t.boolean "public_activity", default: true
    public_activity = fields.BooleanField(default=True)
    # t.boolean "newsletter", default: true
    newsletter = fields.BooleanField(default=True)
    # t.integer "notifications_count", default: 0
    notifications_count = fields.IntField(default=0)
    # t.boolean "registering_with_oauth", default: false
    registering_with_oauth = fields.BooleanField(default=False)
    # t.string "locale"
    locale = fields.CharField(max_length=255, null=True)
    # t.string "oauth_email"
    oauth_email = fields.CharField(max_length=255, null=True)
    # t.integer "geozone_id"
    geozone_id = fields.IntField(null=True)
    # t.string "gender", limit: 10
    gender = fields.CharField(max_length=10, null=True)
    # t.datetime "date_of_birth", precision: nil
    date_of_birth = NaiveDatetimeField(null=True)
    # t.boolean "email_digest", default: true
    email_digest = fields.BooleanField(default=True)
    # t.boolean "email_on_direct_message", default: true
    email_on_direct_message = fields.BooleanField(default=True)
    # t.boolean "official_position_badge", default: false
    official_position_badge = fields.BooleanField(default=False)
    # t.datetime "password_changed_at", precision: nil, default: "2015-01-01 01:01:01", null: false
    password_changed_at = NaiveDatetimeField(null=True)
    # t.boolean "created_from_signature", default: false
    created_from_signature = fields.BooleanField(default=False)
    # t.integer "failed_email_digests_count", default: 0
    failed_email_digests_count = fields.IntField(default=0)
    # t.text "former_users_data_log", default: ""
    former_users_data_log = fields.TextField(default="")
    # t.boolean "public_interests", default: false
    public_interests = fields.BooleanField(default=False)
    # t.boolean "recommended_debates", default: true
    recommended_debates = fields.BooleanField(default=True)
    # t.boolean "recommended_proposals", default: true
    recommended_proposals = fields.BooleanField(default=True)
    # t.string "subscriptions_token"
    subscriptions_token = fields.CharField(max_length=255, null=True)
    # t.integer "failed_attempts", default: 0, null: false
    failed_attempts = fields.IntField(default=0)
    # t.datetime "locked_at", precision: nil
    locked_at = NaiveDatetimeField(null=True)
    # t.string "unlock_token"
    unlock_token = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying DEFAULT ''::character varying,
    encrypted_password character varying DEFAULT ''::character varying NOT NULL,
    reset_password_token character varying,
    reset_password_sent_at timestamp without time zone,
    remember_created_at timestamp without time zone,
    sign_in_count integer DEFAULT 0 NOT NULL,
    current_sign_in_at timestamp without time zone,
    last_sign_in_at timestamp without time zone,
    current_sign_in_ip character varying,
    last_sign_in_ip character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    confirmation_token character varying,
    confirmed_at timestamp without time zone,
    confirmation_sent_at timestamp without time zone,
    unconfirmed_email character varying,
    email_on_comment boolean DEFAULT false,
    email_on_comment_reply boolean DEFAULT false,
    phone_number character varying(30),
    official_position character varying,
    official_level integer DEFAULT 0,
    hidden_at timestamp without time zone,
    sms_confirmation_code character varying,
    username character varying(60),
    document_number character varying,
    document_type character varying,
    residence_verified_at timestamp without time zone,
    email_verification_token character varying,
    verified_at timestamp without time zone,
    unconfirmed_phone character varying,
    confirmed_phone character varying,
    letter_requested_at timestamp without time zone,
    confirmed_hide_at timestamp without time zone,
    letter_verification_code character varying,
    failed_census_calls_count integer DEFAULT 0,
    level_two_verified_at timestamp without time zone,
    erase_reason character varying,
    erased_at timestamp without time zone,
    public_activity boolean DEFAULT true,
    newsletter boolean DEFAULT true,
    notifications_count integer DEFAULT 0,
    registering_with_oauth boolean DEFAULT false,
    locale character varying,
    oauth_email character varying,
    geozone_id integer,
    gender character varying(10),
    date_of_birth timestamp without time zone,
    email_digest boolean DEFAULT true,
    email_on_direct_message boolean DEFAULT true,
    official_position_badge boolean DEFAULT false,
    password_changed_at timestamp without time zone DEFAULT '2015-01-01 01:01:01'::timestamp without time zone NOT NULL,
    created_from_signature boolean DEFAULT false,
    failed_email_digests_count integer DEFAULT 0,
    former_users_data_log text DEFAULT ''::text,
    public_interests boolean DEFAULT false,
    recommended_debates boolean DEFAULT true,
    recommended_proposals boolean DEFAULT true,
    subscriptions_token character varying,
    failed_attempts integer DEFAULT 0 NOT NULL,
    locked_at timestamp without time zone,
    unlock_token character varying
);
"""
