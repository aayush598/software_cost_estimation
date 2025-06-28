"""Top‑level package for software_cost_estimation.

This library provides programmatic APIs to perform software–cost
estimation using well‑known parametric models.

Currently supported models:
* **COCOMO II** – Constructive COnstructive COst MOdel (version 2000).

Future models can be added under :pymod:`software_cost_estimation.models`.
"""

from importlib import metadata

__all__ = [
    "get_version",
]


def get_version() -> str:  # pragma: no cover
    """Return library version string."""
    return metadata.version(__name__)


# Convenience re‑exports
from software_cost_estimation.models.cocomo_ii.model import CocomoIIModel  # noqa: E402  pylint: disable=C0413