from ..models.new_models.delayed_job import NewDelayedJob
from ..models.old_models.delayed_job import OldDelayedJob


async def migrate(id_maps, migration_stats):
    # new fields:
    #   new_delayed_job.tenant
    id_maps["delayed_jobs"] = {}
    stats = {
        "total": 0,
        "migrated": 0,
    }
    old_delayed_jobs = await OldDelayedJob.all()
    new_delayed_jobs = {d.run_at: d for d in await NewDelayedJob.all()}
    for old_delayed_job in old_delayed_jobs:
        stats["total"] += 1
        new_delayed_job = new_delayed_jobs.get(old_delayed_job.run_at)
        if new_delayed_job is None:
            new_delayed_job = NewDelayedJob(run_at=old_delayed_job.run_at)

        new_delayed_job.priority = old_delayed_job.priority
        new_delayed_job.attempts = old_delayed_job.attempts
        new_delayed_job.handler = old_delayed_job.handler
        new_delayed_job.last_error = old_delayed_job.last_error
        new_delayed_job.locked_at = old_delayed_job.locked_at
        new_delayed_job.failed_at = old_delayed_job.failed_at
        new_delayed_job.locked_by = old_delayed_job.locked_by
        new_delayed_job.queue = old_delayed_job.queue
        new_delayed_job.created_at = old_delayed_job.created_at
        new_delayed_job.updated_at = old_delayed_job.updated_at
        # new_delayed_job.tenant = None

        await new_delayed_job.save()
        stats["migrated"] += 1
        id_maps["delayed_jobs"][str(old_delayed_job.id)] = new_delayed_job.id

    migration_stats["delayed_jobs"] = stats
