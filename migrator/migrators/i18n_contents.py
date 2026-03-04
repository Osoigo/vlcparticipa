from ..models.new_models.i18n_content import (
    NewI18nContent,
    NewI18nContentTranslation,
)
from ..models.old_models.i18n_content import (
    OldI18nContent,
    OldI18nContentTranslation,
)


async def migrate(id_maps, migration_stats):
    # new fields:
    id_maps["i18n_contents"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_i18n_contents = await OldI18nContent.all()
    new_i18n_contents = {i.key: i for i in await NewI18nContent.all()}
    for old_i18n_content in old_i18n_contents:
        stats["total"] += 1
        new_i18n_content = new_i18n_contents.get(old_i18n_content.key)
        if new_i18n_content is None:
            new_i18n_content = NewI18nContent(key=old_i18n_content.key)
            await new_i18n_content.save()

        stats["migrated"] += 1
        id_maps["i18n_contents"][str(old_i18n_content.id)] = new_i18n_content.id

    old_i18n_content_translations = await OldI18nContentTranslation.all()
    new_i18n_content_translations = {
        (t.i18n_content_id, t.locale): t for t in await NewI18nContentTranslation.all()
    }
    for old_i18n_content_translation in old_i18n_content_translations:
        new_i18n_content_translation = new_i18n_content_translations.get(
            (
                id_maps["i18n_contents"][
                    str(old_i18n_content_translation.i18n_content_id)
                ],
                old_i18n_content_translation.locale,
            )
        )
        if new_i18n_content_translation is None:
            new_i18n_content_translation = NewI18nContentTranslation(
                i18n_content_id=id_maps["i18n_contents"][
                    str(old_i18n_content_translation.i18n_content_id)
                ],
                locale=old_i18n_content_translation.locale,
            )

        new_i18n_content_translation.created_at = (
            old_i18n_content_translation.created_at
        )
        new_i18n_content_translation.updated_at = (
            old_i18n_content_translation.updated_at
        )
        new_i18n_content_translation.value = old_i18n_content_translation.value

        await new_i18n_content_translation.save()

    migration_stats["i18n_contents"] = stats
