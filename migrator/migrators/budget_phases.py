from datetime import datetime

from ..models.new_models.budget_phase import NewBudgetPhase, NewBudgetPhaseTranslation
from ..models.old_models.budget_phase import OldBudgetPhase


async def migrate(id_maps):
    # new fields:
    #   new_budget_phase_translation.name
    #   new_budget_phase_translation.main_link_text
    #   new_budget_phase_translation.main_link_url
    phase_names = {
        "informing": "Información",
        "accepting": "Presentación de proyectos",
        "reviewing": "Revisión interna de proyectos",
        "selecting": "Fase de apoyos",
        "valuating": "Evaluación de proyectos",
        "publishing_prices": "Publicación de precios",
        "balloting": "Votación final",
        "reviewing_ballots": "Votación finalizada",
        "finished": "Resultados",
        "waiting": "En proceso de publicación de resultados",
    }
    id_maps["budget_phases"] = {}
    old_budget_phases = await OldBudgetPhase.all()
    new_budget_phases = {
        (b.budget_id, b.starts_at): b for b in await NewBudgetPhase.all()
    }
    new_budget_phase_translations = {
        t.budget_phase_id: t for t in await NewBudgetPhaseTranslation.all()
    }
    new_phases = []
    old_phase_transitions = {}
    for old_budget_phase in old_budget_phases:
        if old_budget_phase.kind == "drafting":
            continue
        new_budget_phase = new_budget_phases.get(
            (id_maps["budgets"][old_budget_phase.budget_id], old_budget_phase.starts_at)
        )
        if new_budget_phase is None:
            new_budget_phase = NewBudgetPhase(
                budget_id=id_maps["budgets"][old_budget_phase.budget_id],
                starts_at=old_budget_phase.starts_at,
            )
            new_budget_phase_translation = NewBudgetPhaseTranslation(locale="es")
        else:
            new_budget_phase_translation = new_budget_phase_translations[
                new_budget_phase.id
            ]

        new_budget_phase.budget_id = id_maps["budgets"][old_budget_phase.budget_id]
        new_budget_phase.kind = old_budget_phase.kind
        new_budget_phase.ends_at = old_budget_phase.ends_at
        new_budget_phase.enabled = old_budget_phase.enabled

        await new_budget_phase.save()

        new_phases.append(new_budget_phase)

        new_budget_phase_translation.budget_phase_id = new_budget_phase.id
        new_budget_phase_translation.name = phase_names[old_budget_phase.kind]
        new_budget_phase_translation.description = old_budget_phase.description
        new_budget_phase_translation.summary = old_budget_phase.summary
        new_budget_phase_translation.created_at = datetime.now()
        new_budget_phase_translation.updated_at = datetime.now()
        await new_budget_phase_translation.save()

        id_maps["budget_phases"][old_budget_phase.id] = new_budget_phase.id
        old_phase_transitions[new_budget_phase.id] = old_budget_phase.next_phase_id

    for phase in new_phases:
        old_next_phase = old_phase_transitions[phase.id]
        if old_next_phase is not None:
            phase.next_phase_id = id_maps["budget_phases"][old_next_phase]
            await phase.save()
