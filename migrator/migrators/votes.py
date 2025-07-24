from ..models.new_models.vote import NewVote
from ..models.old_models.vote import OldVote


async def migrate(id_maps, migration_stats):
    # missing in new:
    #   old_vote.refunded_at
    id_maps["votes"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
        "unkonwn_votable_types": set(),
        "unkonwn_voter_types": set(),
        "missing_users": set(),
    }
    old_votes = await OldVote.all()
    new_votes = {(v.votable_id, v.voter_id): v for v in await NewVote.all()}
    for old_vote in old_votes:
        stats["total"] += 1
        if old_vote.votable_type != "Budget::Investment":
            # print(f"Unkonwn vote votable_type: {old_vote.votable_type}")
            stats["unkonwn_votable_types"].add(old_vote.votable_type)
            continue
        if old_vote.voter_type != "User":
            # print(f"Unkonwn vote voter_type: {old_vote.voter_type}")
            stats["unkonwn_voter_types"].add(old_vote.voter_type)
            continue
        user_id = id_maps["users"].get(str(old_vote.voter_id))
        if user_id is None:
            # print(f"Missing user. Old id: {old_vote.voter_id}")
            stats["missing_users"].add(old_vote.voter_id)
            continue
        new_vote = new_votes.get(
            (
                id_maps["budget_investments"][str(old_vote.votable_id)],
                user_id,
            )
        )
        if new_vote is None:
            new_vote = NewVote(
                votable_id=id_maps["budget_investments"][str(old_vote.votable_id)],
                votable_type=old_vote.votable_type,
                voter_id=id_maps["users"][str(old_vote.voter_id)],
                voter_type=old_vote.voter_type,
            )

        new_vote.vote_flag = old_vote.vote_flag
        new_vote.vote_scope = old_vote.vote_scope
        new_vote.vote_weight = old_vote.vote_weight
        new_vote.created_at = old_vote.created_at
        new_vote.updated_at = old_vote.created_at
        new_vote.signature_id = old_vote.signature_id

        await new_vote.save()
        stats["migrated"] += 1
        id_maps["votes"][str(old_vote.id)] = new_vote.id

    stats["unkonwn_votable_types"] = list(stats["unkonwn_votable_types"])
    stats["unkonwn_voter_types"] = list(stats["unkonwn_voter_types"])
    stats["missing_users"] = list(stats["missing_users"])
    migration_stats["votes"] = stats
