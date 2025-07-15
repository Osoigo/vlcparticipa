import hashlib
import shutil
from uuid import uuid4
from base64 import b64encode
from PIL import Image
from ..models.new_models.image import NewImage
from ..models.new_models.active_storage import (
    NewActiveStorageAttachment,
    NewActiveStorageBlob,
)
from ..models.old_models.image import OldImage

from .. import settings


def get_old_image_path(old_image):
    id_str = f"{old_image.id:09}"
    id_partition = "/".join(id_str[i : i + 3] for i in range(0, len(id_str), 3))
    hash = "60570d0e6aa151fd2dae36190583d356e455fd23"
    extension = old_image.attachment_file_name.rsplit(".", 1)[1]
    return f"system/images/attachments/{id_partition}/original/{hash}.{extension}"


async def migrate(id_maps):
    id_maps["images"] = {}
    id_maps["active_storage_attachments"] = {}
    id_maps["active_storage_blobs"] = {}
    old_images = await OldImage.all()
    new_images = {
        (i.imageable_id, i.imageable_type, i.title): i for i in await NewImage.all()
    }
    new_active_storage_attachments = {
        a.record_id: a
        for a in await NewActiveStorageAttachment.filter(record_type="Image")
    }
    new_active_storage_blobs = {a.id: a for a in await NewActiveStorageBlob.all()}
    for old_image in old_images:
        if old_image.imageable_type == "Budget":
            imageable_id = id_maps["budgets"][old_image.imageable_id]
        elif old_image.imageable_type == "Budget::Investment":
            imageable_id = id_maps["budget_investments"][old_image.imageable_id]
        # TODO: elif old_image.imageable_type == "Budget::Investment::Milestone":
        #   imageable_id = id_maps["budget_investment_milestones"][old_image.imageable_id]
        else:
            continue
        new_image = new_images.get(
            (imageable_id, old_image.imageable_type, old_image.title)
        )
        if new_image is None:
            new_image = NewImage(
                imageable_id=imageable_id,
                imageable_type=old_image.imageable_type,
                title=old_image.title,
            )
            active_storage_attachment = NewActiveStorageAttachment(
                record_type="Image",
                name="attachment",
            )
            active_storage_blob = NewActiveStorageBlob(
                service_name="local",
                key=str(uuid4()).replace("-", ""),
            )
        else:
            active_storage_attachment = new_active_storage_attachments[new_image.id]
            active_storage_blob = new_active_storage_blobs[
                active_storage_attachment.blob_id
            ]
        new_image.title = old_image.title
        new_image.created_at = old_image.created_at
        new_image.updated_at = old_image.updated_at
        new_image.user_id = id_maps["users"][old_image.user_id]

        await new_image.save()

        old_image_path = settings.OLD_STORAGE_PATH / get_old_image_path(old_image)
        old_image_file = Image.open(old_image_path)
        img_width, img_height = old_image_file.size
        active_storage_blob.filename = old_image.attachment_file_name
        active_storage_blob.content_type = old_image.attachment_content_type
        active_storage_blob.metadata = f'{{"identified":true,"width":{img_width},"height":{img_height},"analyzed":true}}'
        active_storage_blob.byte_size = old_image.attachment_file_size
        with old_image_path.open("rb") as f:
            active_storage_blob.checksum = b64encode(
                hashlib.md5(f.read()).digest()
            ).decode()
        active_storage_blob.created_at = new_image.created_at
        await active_storage_blob.save()

        active_storage_attachment.record_id = new_image.id
        active_storage_attachment.created_at = old_image.attachment_updated_at
        active_storage_attachment.blob_id = active_storage_blob.id
        await active_storage_attachment.save()

        new_image_path = (
            settings.NEW_STORAGE_PATH
            / f"{active_storage_blob.key[0:2]}/{active_storage_blob.key[2:4]}/{active_storage_blob.key}"
        )
        if not new_image_path.parent.exists():
            new_image_path.parent.mkdir(parents=True)
        print(f"Copy {old_image_path} to {new_image_path}")
        shutil.copy(old_image_path, new_image_path)

        id_maps["images"][old_image.id] = new_image.id
        id_maps["active_storage_attachments"][old_image.id] = (
            active_storage_attachment.id
        )
        id_maps["active_storage_blobs"][old_image.id] = active_storage_blob.id
