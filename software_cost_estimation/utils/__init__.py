"""Miscellaneous helpers (logger, conversions, etc.)."""

from .logger import get_logger  # noqa: F401  (re‑export)


# -----------------------------------------------------
# File: software_cost_estimation/utils/logger.py
# -----------------------------------------------------
"""Tiny convenience wrapper around :pymod:`logging`."""

from __future__ import annotations

import logging


def get_logger(name: str) -> logging.Logger:  # pragma: no cover
    logging.basicConfig(
        format="%(levelname)s | %(name)s | %(message)s",
        level=logging.INFO,
    )
    return logging.getLogger(name)
