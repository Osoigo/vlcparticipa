from tortoise.models import Model
from tortoise import fields

from ...custom_fields import NaiveDatetimeField


class NewActiveStorageAttachment(Model):
    class Meta:
        table = "active_storage_attachments"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string "name", null: false
    name = fields.CharField(max_length=255)
    # t.string "record_type", null: false
    record_type = fields.CharField(max_length=255)
    # t.bigint "record_id", null: false
    record_id = fields.BigIntField()
    # t.bigint "blob_id", null: false
    blob_id = fields.BigIntField()
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()


"""
CREATE TABLE public.active_storage_attachments (
    id bigint NOT NULL,
    name character varying NOT NULL,
    record_type character varying NOT NULL,
    record_id bigint NOT NULL,
    blob_id bigint NOT NULL,
    created_at timestamp without time zone NOT NULL
);
"""


class NewActiveStorageBlob(Model):
    class Meta:
        table = "active_storage_blobs"
        app = "new"

    id = fields.IntField(primary_key=True)
    # t.string "key", null: false
    key = fields.CharField(max_length=255)
    # t.string "filename", null: false
    filename = fields.CharField(max_length=255)
    # t.string "content_type"
    content_type = fields.CharField(max_length=255, null=True)
    # t.text "metadata"
    metadata = fields.TextField(null=True)
    # t.bigint "byte_size", null: false
    byte_size = fields.BigIntField()
    # t.string "checksum"
    checksum = fields.CharField(max_length=255, null=True)
    # t.datetime "created_at", precision: nil, null: false
    created_at = NaiveDatetimeField()
    # t.string "service_name", null: false
    service_name = fields.CharField(max_length=255)


"""
CREATE TABLE public.active_storage_blobs (
    id bigint NOT NULL,
    key character varying NOT NULL,
    filename character varying NOT NULL,
    content_type character varying,
    metadata text,
    byte_size bigint NOT NULL,
    checksum character varying,
    created_at timestamp without time zone NOT NULL,
    service_name character varying NOT NULL
);
"""
