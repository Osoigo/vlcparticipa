from datetime import datetime

from ..models.new_models.comment import NewComment, NewCommentTranslation
from ..models.old_models.comment import OldComment


async def migrate(id_maps):
    id_maps["comments"] = {}
    old_root_comments = await OldComment.filter(ancestry=None)
    old_nonroot_comments = await OldComment.exclude(ancestry=None).order_by("ancestry")
    old_comments = old_root_comments + old_nonroot_comments
    new_comments = {
        (c.commentable_id, c.commentable_type, c.created_at): c
        for c in await NewComment.all()
    }
    new_comment_translations = {
        t.comment_id: t for t in await NewCommentTranslation.all()
    }
    for old_comment in old_comments:
        if old_comment.commentable_type == "Budget::Investment":
            commentable_id = id_maps["budget_investments"][
                str(old_comment.commentable_id)
            ]
        else:
            print(f"Comentario en elemento desconocido: {old_comment.commentable_type}")
            continue
        new_comment = new_comments.get(
            (commentable_id, old_comment.commentable_type, old_comment.created_at)
        )
        if new_comment is None:
            new_comment = NewComment(
                commentable_id=commentable_id,
                commentable_type=old_comment.commentable_type,
                created_at=old_comment.created_at,
            )
            new_comment_translation = NewCommentTranslation(locale="es")
        else:
            new_comment_translation = new_comment_translations[new_comment.id]

        new_comment.subject = old_comment.subject
        new_comment.user_id = id_maps["users"][str(old_comment.user_id)]
        new_comment.updated_at = old_comment.updated_at
        new_comment.hidden_at = old_comment.hidden_at
        new_comment.flags_count = old_comment.flags_count
        new_comment.ignored_flag_at = old_comment.ignored_flag_at
        new_comment.moderator_id = None  # Es null siempre en producción
        if old_comment.administrator_id is not None:
            administrator_id = id_maps["administrators"].get(
                str(old_comment.administrator_id)
            )
            if administrator_id is None:
                print(f"Missing administrator. Old id: {old_comment.administrator_id}")
            new_comment.administrator_id = administrator_id
        else:
            new_comment.administrator_id = None
        new_comment.cached_votes_total = old_comment.cached_votes_total
        new_comment.cached_votes_up = old_comment.cached_votes_up
        new_comment.cached_votes_down = old_comment.cached_votes_down
        new_comment.confirmed_hide_at = old_comment.confirmed_hide_at
        new_comment.confidence_score = old_comment.confidence_score
        new_comment.valuation = old_comment.valuation

        ancestors = []
        if old_comment.ancestry is not None:
            ancestors = [
                str(id_maps["comments"][comment_id])
                for comment_id in old_comment.ancestry.split("/")
            ]

        if ancestors:
            new_comment.ancestry = "/".join(ancestors)

        new_comment.tsv = None  # TODO: mirar apps/models/concerns/search_cache.rb, método search_values_sql

        await new_comment.save()

        new_comment_translation.comment_id = new_comment.id
        new_comment_translation.created_at = datetime.now()
        new_comment_translation.updated_at = datetime.now()
        new_comment_translation.body = old_comment.body
        await new_comment_translation.save()

        id_maps["comments"][str(old_comment.id)] = new_comment.id
