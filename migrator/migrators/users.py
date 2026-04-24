from ..models.new_models.user import NewUser
from ..models.old_models.user import OldUser


async def migrate(id_maps, migration_stats):
    # missing in new:
    #   old_user.redeemable_code
    #   old_user.email_on_proposal_notification
    #   old_user.activo
    #   old_user.district_wide_spending_proposals_supported_count
    #   old_user.city_wide_spending_proposals_supported_count
    #   old_user.supported_spending_proposals_geozone_id
    #   old_user.dni_presencial
    #   old_user.auth_token
    #   old_user.security_question_id
    #   old_user.security_question_answer
    #   old_user.verification_confirmed_at
    #
    # new fields:
    #   new_user.subscriptions_token
    #   new_user.failed_attempts
    #   new_user.locked_at
    #   new_user.unlock_token
    id_maps["users"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
        "not_migrated_users": list(),
    }
    old_users = await OldUser.all()
    new_users = {(u.email, u.created_at, u.erased_at): u for u in await NewUser.all()}
    for idx, old_user in enumerate(old_users):
        stats["total"] += 1
        new_user = new_users.get(
            (old_user.email, old_user.created_at, old_user.erased_at)
        )
        if new_user is None:
            new_user = NewUser(
                email=old_user.email,
                created_at=old_user.created_at,
                erased_at=old_user.erased_at,
            )
        new_user.encrypted_password = old_user.encrypted_password
        new_user.reset_password_token = old_user.reset_password_token
        new_user.reset_password_sent_at = old_user.reset_password_sent_at
        new_user.remember_created_at = old_user.remember_created_at
        new_user.sign_in_count = old_user.sign_in_count
        new_user.current_sign_in_at = old_user.current_sign_in_at
        new_user.last_sign_in_at = old_user.last_sign_in_at
        new_user.updated_at = old_user.updated_at
        new_user.confirmation_token = old_user.confirmation_token
        new_user.confirmed_at = old_user.confirmed_at
        new_user.confirmation_sent_at = old_user.confirmation_sent_at
        new_user.unconfirmed_email = old_user.unconfirmed_email
        new_user.email_on_comment = old_user.email_on_comment
        new_user.email_on_comment_reply = old_user.email_on_comment_reply
        new_user.official_position = old_user.official_position
        new_user.official_level = old_user.official_level
        new_user.hidden_at = old_user.hidden_at
        new_user.sms_confirmation_code = old_user.sms_confirmation_code
        new_user.username = old_user.username
        new_user.document_number = old_user.document_number
        new_user.document_type = old_user.document_type
        new_user.residence_verified_at = old_user.residence_verified_at
        new_user.email_verification_token = old_user.email_verification_token
        new_user.verified_at = old_user.verified_at
        new_user.unconfirmed_phone = old_user.unconfirmed_phone
        new_user.confirmed_phone = old_user.confirmed_phone
        new_user.letter_requested_at = old_user.letter_requested_at
        new_user.confirmed_hide_at = old_user.confirmed_hide_at
        new_user.letter_verification_code = old_user.letter_verification_code
        new_user.failed_census_calls_count = old_user.failed_census_calls_count
        new_user.level_two_verified_at = old_user.level_two_verified_at
        new_user.erase_reason = old_user.erase_reason
        new_user.public_activity = old_user.public_activity
        new_user.newsletter = old_user.newsletter
        new_user.notifications_count = old_user.notifications_count
        new_user.registering_with_oauth = old_user.registering_with_oauth
        new_user.locale = old_user.locale
        new_user.oauth_email = old_user.oauth_email
        new_user.geozone_id = old_user.geozone_id
        new_user.gender = old_user.gender
        new_user.email_digest = old_user.email_digest
        new_user.email_on_direct_message = old_user.email_on_direct_message
        new_user.official_position_badge = old_user.official_position_badge
        new_user.password_changed_at = old_user.password_changed_at
        new_user.created_from_signature = old_user.created_from_signature
        new_user.failed_email_digests_count = old_user.failed_email_digests_count
        new_user.former_users_data_log = old_user.former_users_data_log
        new_user.public_interests = old_user.public_interests
        new_user.recommended_debates = old_user.recommended_debates
        new_user.recommended_proposals = old_user.recommended_proposals
        new_user.nIA = old_user.nIA
        new_user.name = old_user.name
        new_user.first_name = old_user.first_name
        new_user.last_name = old_user.last_name
        new_user.municipality_of_birth = old_user.municipality_of_birth
        new_user.province_of_birth = old_user.province_of_birth
        new_user.country_of_birth = old_user.country_of_birth
        new_user.nationality = old_user.nationality
        new_user.dc = old_user.dc
        new_user.census_last_modification_at = old_user.census_last_modification_at
        new_user.district = old_user.district
        new_user.section = old_user.section
        new_user.sheet_number = old_user.sheet_number
        new_user.census_created_at = old_user.census_created_at
        new_user.collective_entity = old_user.collective_entity
        new_user.singular_entity = old_user.singular_entity
        new_user.core = old_user.core
        new_user.single_entity_code = old_user.single_entity_code
        new_user.census_phone = old_user.census_phone
        new_user.level_of_training = old_user.level_of_training
        new_user.permit_expiration_at = old_user.permit_expiration_at
        new_user.province = old_user.province
        new_user.municipality = old_user.municipality
        new_user.acronym = old_user.acronym
        new_user.type_road = old_user.type_road
        new_user.street_name = old_user.street_name
        new_user.access = old_user.access
        new_user.km = old_user.km
        new_user.stairs = old_user.stairs
        new_user.floor = old_user.floor
        new_user.door = old_user.door
        new_user.zip_code = old_user.zip_code
        new_user.full_address = old_user.full_address
        new_user.protected_hab = old_user.protected_hab
        try:
            await new_user.save()
            stats["migrated"] += 1
            id_maps["users"][str(old_user.id)] = new_user.id
            print(idx, end="\r")
        except Exception as e:
            stats["not_migrated_users"].append(old_user.id)
            print("X")
    print("")
    migration_stats["users"] = stats
