"""Dynamic model discovery utilities."""

from importlib import import_module
from typing import Dict, Type

from software_cost_estimation.core.base_model import BaseModel

__all__ = ["get_model_registry"]


# Registry will lazily load models on first call
_MODEL_REGISTRY: Dict[str, Type[BaseModel]] | None = None


def _discover_models() -> Dict[str, Type[BaseModel]]:  # pragma: no cover
    """Import sub‑packages under *models* so they register themselves."""

    import pkgutil
    import pathlib

    here = pathlib.Path(__file__).parent
    modules = {}
    for mod in pkgutil.iter_modules([str(here)]):
        if not mod.ispkg:
            continue
        pkg_name = f"{__name__}.{mod.name}.model"
        try:
            module = import_module(pkg_name)
            cls = getattr(module, module.__all__[0])  # type: ignore[index]
            modules[cls.model_name] = cls
        except Exception:  # pragma: no cover
            # Skip broken or partial modules
            continue
    return modules


def get_model_registry() -> Dict[str, Type[BaseModel]]:  # pragma: no cover
    global _MODEL_REGISTRY  # pylint: disable=global-statement
    if _MODEL_REGISTRY is None:
        _MODEL_REGISTRY = _discover_models()
    return _MODEL_REGISTRY
