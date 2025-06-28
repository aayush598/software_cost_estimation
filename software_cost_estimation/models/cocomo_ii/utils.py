"""Helper math for COCOMO II model."""

from __future__ import annotations

import functools
from typing import Dict

from ...core.validators import validate_ratings
from .parameters import (  # noqa: WPS347 (relative import fine inside package)
    A,
    B,
    C,
    D,
    EMTable,
    ScaleTable,
    EM_KEYS,
    SCALE_KEYS,
)


# ---------------------------------------------------------------------------
# Scale‑factor calculations
# ---------------------------------------------------------------------------

def calc_e(scale_ratings: Dict[str, str]) -> float:
    """Compute the *E* exponent from user‑supplied scale‑factor ratings."""
    validate_ratings("ScaleFactor", scale_ratings, SCALE_KEYS)
    sf_sum = sum(ScaleTable[key][code] for key, code in scale_ratings.items())
    return B + 0.01 * sf_sum


# ---------------------------------------------------------------------------
# Effort multipliers
# ---------------------------------------------------------------------------

def calc_em_product(em_ratings: Dict[str, str]) -> float:
    """Multiply all 17 effort multipliers together."""
    validate_ratings("EffortMultiplier", em_ratings, EM_KEYS)
    return functools.reduce(
        lambda acc, kv: acc * EMTable[kv[0]][kv[1]],
        em_ratings.items(),
        1.0,
    )


# ---------------------------------------------------------------------------
# Primary model equations
# ---------------------------------------------------------------------------

def calc_person_months(size: float, E: float, em_prod: float) -> float:
    """COCOMO II effort equation (Equation 11)."""
    return A * (size ** E) * em_prod


def calc_time_months(PM: float, E: float) -> float:
    """Nominal‑schedule duration (Equation 2).

    SCED multiplier already factored into *PM*.
    """
    return C * (PM ** (D + 0.2 * (E - B)))
