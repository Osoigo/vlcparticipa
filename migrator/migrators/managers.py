from ..models.new_models.manager import NewManager
from ..models.old_models.manager import OldManager


async def migrate(id_maps):
    user_map = id_maps["users"]
    id_maps["managers"] = {}
    old_managers = await OldManager.all()
    new_managers = {v.user_id: v for v in await NewManager.all()}
    for old_manager in old_managers:
        new_manager = new_managers.get(user_map[old_manager.user_id])
        if new_manager is None:
            new_manager = NewManager(user_id=user_map[old_manager.user_id])
        await new_manager.save()
        id_maps["managers"][old_manager.id] = new_manager.id
