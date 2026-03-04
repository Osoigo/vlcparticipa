from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class OldI18nContent(Model):
    class Meta:
        table = "i18n_contents"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.string "key"
    key = fields.CharField(max_length=255, null=True)


"""
CREATE TABLE public.i18n_contents (
    id integer NOT NULL,
    key character varying
);
"""


class OldI18nContentTranslation(Model):
    class Meta:
        table = "i18n_content_translations"
        app = "old"

    id = fields.IntField(primary_key=True)
    # t.integer "i18n_content_id", null: false
    i18n_content_id = fields.IntField()
    # t.string "locale", null: false
    locale = fields.CharField(max_length=255)
    # t.datetime "created_at", null: false
    created_at = NaiveDatetimeField()
    # t.datetime "updated_at", null: false
    updated_at = NaiveDatetimeField()
    # t.text "value"
    value = fields.TextField()


"""
CREATE TABLE public.i18n_content_translations (
    id integer NOT NULL,
    i18n_content_id integer NOT NULL,
    locale character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    value text
);
"""
