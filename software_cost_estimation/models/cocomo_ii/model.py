"""Concrete implementation of the COCOMO II (2000) Post‑Architecture model."""

from __future__ import annotations

from typing import Final

from ...core.base_model import BaseModel
from ...core.types import EstimationInput, EstimationResult
from . import utils as _u
from .parameters import EM_KEYS, SCALE_KEYS


class CocomoIIModel(BaseModel):
    """COCOMO II cost‑estimation model implementation."""

    model_name: Final[str] = "COCOMO II"

    # ------------------------------------------------------------------
    # BaseModel implementation
    # ------------------------------------------------------------------
    def estimate(self, inputs: EstimationInput) -> EstimationResult:  # noqa: D401
        """Estimate Person‑Months and schedule given *inputs*."""

        # 1) Exponent E
        E = _u.calc_e(inputs.scale_factors)

        # 2) Effort multipliers product (includes SCED)
        em_prod = _u.calc_em_product(inputs.effort_multipliers)

        # 3) Core equations
        PM = _u.calc_person_months(inputs.size_ksloc, E, em_prod)
        TDEV = _u.calc_time_months(PM, E)
        avg_staff = PM / TDEV if TDEV else 0.0

        return EstimationResult(PM, TDEV, avg_staff)

    # ------------------------------------------------------------------
    # Convenience helpers
    # ------------------------------------------------------------------
    @staticmethod
    def required_rating_keys() -> dict[str, tuple[str, ...]]:  # pragma: no cover
        """Return lists of required scale‑factor and EM keys for UI builders."""
        return {"scale_factors": SCALE_KEYS, "effort_multipliers": EM_KEYS}
