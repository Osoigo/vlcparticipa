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
from .budget_valuator_assignment import OldBudgetValuatorAssignment
from .comment import OldComment
from .community import OldCommunity
from .document import OldDocument
from .geozone import OldGeozone
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
    "OldBudgetValuatorAssignment",
    "OldComment",
    "OldCommunity",
    "OldDocument",
    "OldGeozone",
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
