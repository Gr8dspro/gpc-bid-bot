from enum import Enum
from typing import Tuple

class Stage(str, Enum):
    PARSED = "PARSED"
    OFFERED = "OFFERED"
    SCORED = "SCORED"
    QUOTED = "QUOTED"

_ALLOWED: Tuple[Tuple[Stage,Stage], ...] = (
    (Stage.PARSED, Stage.OFFERED),
    (Stage.OFFERED, Stage.SCORED),
    (Stage.SCORED, Stage.QUOTED),
)

def validate_transition(old: Stage, new: Stage) -> bool:
    return (old, new) in _ALLOWED
