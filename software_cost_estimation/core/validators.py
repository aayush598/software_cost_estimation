"""Simple runtime validation helpers."""

from __future__ import annotations

from typing import Mapping, Sequence


class ValidationError(RuntimeError):
    """Raised when user input is missing or malformed."""


_RATING_CODES: Sequence[str] = ("VL", "L", "N", "H", "VH", "XH")


def validate_ratings(model_key: str, supplied: Mapping[str, str], expected: Sequence[str]) -> None:
    """Ensure *supplied* contains all *expected* keys with legal codes."""

    missing = sorted(set(expected) - supplied.keys())
    if missing:
        raise ValidationError(
            f"{model_key}: missing rating(s) for {', '.join(missing)}"
        )

    for key, code in supplied.items():
        if code not in _RATING_CODES:
            raise ValidationError(
                f"{model_key}: illegal rating code '{code}' for key '{key}'"
            )

