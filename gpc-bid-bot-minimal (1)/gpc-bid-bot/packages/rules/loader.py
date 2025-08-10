from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Any
import yaml, pathlib

@dataclass(frozen=True)
class Rules:
    include: List[str]
    exclude: List[str]
    thresholds: Dict[str, Any]

def load_rules(path: str = "packages/rules/schema.yaml") -> Rules:
    p = pathlib.Path(path)
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    return Rules(
        include=list(data.get("include", [])),
        exclude=list(data.get("exclude", [])),
        thresholds=dict(data.get("thresholds", {})),
    )
