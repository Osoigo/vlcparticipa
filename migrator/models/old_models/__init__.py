from .activity import OldActivity
from .administrator import OldAdministrator
from .budget import OldBudget
from .budget_ballot import OldBudgetBallot, OldBudgetBallotLine
from .budget_group import OldBudgetGroup
from .budget_heading import OldBudgetHeading
from .budget_investment import OldBudgetInvestment
from .budget_investment_milestone import (
    OldBudgetInvestmentStatus,
    OldBudgetInvestmentMilestone,
    OldBudgetInvestmentMilestoneTranslation,
)
from .budget_phase import OldBudgetPhase
from .budget_reclassified_vote import OldBudgetReclasifiedVote
from .budget_valuator_assignment import OldBudgetValuatorAssignment
from .comment import OldComment
from .community import OldCommunity
from .delayed_job import OldDelayedJob
from .document import OldDocument
from .failed_census_call import OldFailedCensusCall
from .geozone import OldGeozone
from .i18n_content import OldI18nContent, OldI18nContentTranslation
from .image import OldImage
from .manager import OldManager
from .map_location import OldMapLocation
from .newsletter import OldNewsletter
from .tag import OldTag, OldTaggings
from .user import OldUser
from .valuator import OldValuator
from .visit import OldVisit
from .vote import OldVote

__all__ = [
    "OldAdministrator",
    "OldActivity",
    "OldBudget",
    "OldBudgetBallot",
    "OldBudgetBallotLine",
    "OldBudgetGroup",
    "OldBudgetHeading",
    "OldBudgetInvestment",
    "OldBudgetInvestmentStatus",
    "OldBudgetInvestmentMilestone",
    "OldBudgetInvestmentMilestoneTranslation",
    "OldBudgetPhase",
    "OldBudgetReclasifiedVote",
    "OldBudgetValuatorAssignment",
    "OldComment",
    "OldCommunity",
    "OldDelayedJob",
    "OldDocument",
    "OldFailedCensusCall",
    "OldGeozone",
    "OldI18nContent",
    "OldI18nContentTranslation",
    "OldImage",
    "OldManager",
    "OldMapLocation",
    "OldNewsletter",
    "OldTag",
    "OldTaggings",
    "OldUser",
    "OldValuator",
    "OldVisit",
    "OldVote",
]
