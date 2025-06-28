"""Lightweight dataclass containers for input and output."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


RatingMap = Dict[str, str]  # e.g. {"PREC": "N", "RELY": "VH"}


@dataclass(slots=True)
class EstimationInput:
    """User‑supplied data needed by every model.

    Parameters
    ----------
    size_ksloc
        Estimated code size in *thousands* of source lines of code.
    scale_factors
        Mapping *scale‑factor key* → *rating code* (e.g. ``"PREC": "VL"``).
    effort_multipliers
        Mapping *EM key* → *rating code* (e.g. ``"TIME": "H"``).
    """

    size_ksloc: float
    scale_factors: RatingMap
    effort_multipliers: RatingMap


@dataclass(slots=True)
class EstimationResult:
    """Computed effort and schedule results."""

    person_months: float
    time_months: float
    avg_staff: float

    def as_dict(self) -> dict:  # pragma: no cover
        """Return a JSON‑serialisable view."""
        return {
            "person_months": round(self.person_months, 3),
            "time_months": round(self.time_months, 3),
            "average_staff": round(self.avg_staff, 3),
        }
