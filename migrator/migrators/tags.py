from ..models.new_models.tag import NewTag, NewTaggings
from ..models.old_models.tag import OldTag, OldTaggings


async def migrate(id_maps):
    # missing in new:
    #   old_tag.spending_proposals_count
    #   old_tag.featured
    id_maps["tags"] = {}
    old_tags = await OldTag.all()
    new_tags = {g.name: g for g in await NewTag.all()}
    for old_tag in old_tags:
        new_tag = new_tags.get(old_tag.name)
        if new_tag is None:
            new_tag = NewTag(name=old_tag.name)

        new_tag.taggings_count = old_tag.taggings_count
        new_tag.debates_count = old_tag.debates_count
        new_tag.proposals_count = old_tag.proposals_count
        new_tag.kind = old_tag.kind
        new_tag.budget_investments_count = old_tag.budget_investments_count
        new_tag.legislation_proposals_count = old_tag.legislation_proposals_count
        new_tag.legislation_processes_count = old_tag.legislation_processes_count

        await new_tag.save()

        id_maps["tags"][old_tag.id] = new_tag.id

    id_maps["taggings"] = {}
    old_taggings = await OldTaggings.all()
    new_taggings = {(t.tag_id, t.taggable_id): t for t in await NewTaggings.all()}
    for old_tagging in old_taggings:
        if old_tagging.taggable_type != "Budget::Investment":
            print(f"Unkonwn tagging: {old_tagging.taggable_type}")
            continue
        new_tagging = new_taggings.get(
            (
                id_maps["tags"][old_tagging.tag_id],
                old_tagging.taggable_id,
            )
        )
        if new_tagging is None:
            new_tagging = NewTaggings(
                tag_id=id_maps["tags"][old_tagging.tag_id],
                taggable_type=old_tagging.taggable_type,
            )

        new_tagging.taggable_id = (
            old_tagging.taggable_id
        )  # Investment ids are the same in both databases
        new_tagging.taggable_type = old_tagging.taggable_type
        new_tagging.tagger_id = old_tagging.tagger_id  # Not used in old, always blank
        new_tagging.tagger_type = old_tagging.tagger_type
        new_tagging.context = old_tagging.context
        new_tagging.created_at = old_tagging.created_at

        await new_tagging.save()

        id_maps["taggings"][old_tagging.id] = new_tagging.id
