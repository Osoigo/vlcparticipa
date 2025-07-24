from ..models.new_models.newsletter import NewNewsletter
from ..models.old_models.newsletter import OldNewsletter


async def migrate(id_maps, migration_stats):
    id_maps["newsletters"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_newsletters = await OldNewsletter.all()
    new_newsletters = {
        (n.created_at, n.segment_recipient): n for n in await NewNewsletter.all()
    }
    for old_newsletter in old_newsletters:
        stats["total"] += 1
        new_newsletter = new_newsletters.get(
            (old_newsletter.created_at, old_newsletter.segment_recipient)
        )
        if new_newsletter is None:
            new_newsletter = NewNewsletter(
                created_at=old_newsletter.created_at,
                segment_recipient=old_newsletter.segment_recipient,
            )

        new_newsletter.subject = old_newsletter.subject
        new_newsletter._from = old_newsletter._from
        new_newsletter.body = old_newsletter.body
        new_newsletter.sent_at = old_newsletter.sent_at
        new_newsletter.updated_at = old_newsletter.updated_at
        new_newsletter.hidden_at = old_newsletter.hidden_at

        await new_newsletter.save()
        stats["migrated"] += 1
        id_maps["newsletters"][str(old_newsletter.id)] = new_newsletter.id

    migration_stats["newsletters"] = stats
