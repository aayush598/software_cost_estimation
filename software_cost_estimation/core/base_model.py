"""Abstract base class that every cost‑estimation model must implement."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar

from .types import EstimationInput, EstimationResult


class BaseModel(ABC):
    """Abstract parametric cost‑estimation model."""

    #: Human‑readable model identifier, e.g. ``"COCOMO II"``.
    model_name: ClassVar[str]

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    @abstractmethod
    def estimate(self, inputs: EstimationInput) -> EstimationResult:
        """Run the model and return an :class:`EstimationResult`."""

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def __call__(self, inputs: EstimationInput) -> EstimationResult:  # pragma: no cover
        """Syntactic sugar so instances are callable."""
        return self.estimate(inputs)

