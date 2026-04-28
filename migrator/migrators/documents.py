import hashlib
import shutil
from uuid import uuid4
from base64 import b64encode
from pathlib import Path
from ..models.new_models.document import NewDocument
from ..models.new_models.active_storage import (
    NewActiveStorageAttachment,
    NewActiveStorageBlob,
)
from ..models.old_models.document import OldDocument

from .. import settings


def get_old_document_path(old_document):
    id_str = f"{old_document.id:09}"
    id_partition = "/".join(id_str[i : i + 3] for i in range(0, len(id_str), 3))
    # hash = "60570d0e6aa151fd2dae36190583d356e455fd23"  # dev_seed
    hash = "f23035fa8edfd5a3ad1da3dabc634d17bed8a6c0"  # production
    extension = old_document.attachment_file_name.rsplit(".", 1)[1]
    return f"system/documents/attachments/{id_partition}/original/{hash}.{extension}"

def get_old_document_alternative_path(old_document):
    return f"system/documents/cached_attachments/user/{old_document.user_id}/original/{old_document.attachment_file_name}"


async def migrate(id_maps, migration_stats):
    id_maps["documents"] = {}
    id_maps["active_storage_attachments"] = {}
    id_maps["active_storage_blobs"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
        "missing_document_files": list(),
    }
    old_documents = await OldDocument.all()
    new_documents = {
        (i.documentable_id, i.documentable_type, i.title): i
        for i in await NewDocument.all()
    }
    new_active_storage_attachments = {
        a.record_id: a
        for a in await NewActiveStorageAttachment.filter(record_type="Document")
    }
    new_active_storage_blobs = {a.id: a for a in await NewActiveStorageBlob.all()}
    for old_document in old_documents:
        stats["total"] += 1
        old_document_path = Path(
            settings.OLD_STORAGE_PATH / get_old_document_path(old_document)
        )
        if not old_document_path.exists():
            old_document_path = Path(
                settings.OLD_STORAGE_PATH / get_old_document_alternative_path(old_document)
            )
            if not old_document_path.exists():
                print(f"Missing document file: {get_old_document_path(old_document)}, {get_old_document_alternative_path(old_document)}")
                stats["missing_document_files"].append((get_old_document_path(old_document), get_old_document_alternative_path(old_document)))
                continue
        if old_document.documentable_type == "Budget::Investment":
            documentable_id = id_maps["budget_investments"][
                str(old_document.documentable_id)
            ]
        else:
            continue
        new_document = new_documents.get(
            (documentable_id, old_document.documentable_type, old_document.title)
        )
        if new_document is None:
            new_document = NewDocument(
                documentable_id=documentable_id,
                documentable_type=old_document.documentable_type,
                title=old_document.title,
            )
            active_storage_attachment = NewActiveStorageAttachment(
                record_type="Document",
                name="attachment",
            )
            active_storage_blob = NewActiveStorageBlob(
                service_name="local",
                key=str(uuid4()).replace("-", ""),
            )
        else:
            active_storage_attachment = new_active_storage_attachments.get(new_document.id)
            if active_storage_attachment is None:
                active_storage_attachment = NewActiveStorageAttachment(
                    record_type="Document",
                    name="attachment",
                )
            active_storage_blob = new_active_storage_blobs.get(active_storage_attachment.blob_id)
            if active_storage_blob is None:
                active_storage_blob = NewActiveStorageBlob(
                    service_name="local",
                    key=str(uuid4()).replace("-", ""),
                )
        new_document.created_at = old_document.created_at
        new_document.updated_at = old_document.updated_at
        new_document.user_id = id_maps["users"][str(old_document.user_id)]

        await new_document.save()

        active_storage_blob.filename = old_document.attachment_file_name
        active_storage_blob.content_type = old_document.attachment_content_type
        active_storage_blob.metadata = '{"identified":true,"analyzed":true}'
        active_storage_blob.byte_size = old_document.attachment_file_size
        with old_document_path.open("rb") as f:
            active_storage_blob.checksum = b64encode(
                hashlib.md5(f.read()).digest()
            ).decode()
        active_storage_blob.created_at = new_document.created_at
        await active_storage_blob.save()

        active_storage_attachment.record_id = new_document.id
        active_storage_attachment.created_at = old_document.attachment_updated_at
        active_storage_attachment.blob_id = active_storage_blob.id
        await active_storage_attachment.save()

        new_document_path = (
            settings.NEW_STORAGE_PATH
            / f"{active_storage_blob.key[0:2]}/{active_storage_blob.key[2:4]}/{active_storage_blob.key}"
        )
        if not new_document_path.parent.exists():
            new_document_path.parent.mkdir(parents=True)
        # print(f"Copy {old_document_path} to {new_document_path}")
        shutil.copy(old_document_path, new_document_path)

        stats["migrated"] += 1
        id_maps["documents"][str(old_document.id)] = new_document.id
        id_maps["active_storage_attachments"][str(old_document.id)] = (
            active_storage_attachment.id
        )
        id_maps["active_storage_blobs"][str(old_document.id)] = active_storage_blob.id

    migration_stats["documents"] = stats
