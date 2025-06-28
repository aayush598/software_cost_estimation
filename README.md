"""High‑level documentation for the package."""

# software_cost_estimation

> A modular Python library that implements the **COCOMO II** software‑cost estimation model, with a plug‑in architecture for adding future models.

```bash
pip install software_cost_estimation
```

```python
from software_cost_estimation import CocomoIIModel
from software_cost_estimation.core.types import EstimationInput

scale = {"PREC": "N", "FLEX": "N", "RESL": "N", "TEAM": "N", "PMAT": "N"}
em = {key: "N" for key in CocomoIIModel.required_rating_keys()["effort_multipliers"]}

result = CocomoIIModel()(EstimationInput(100.0, scale, em))
print(result)
# EstimationResult(person_months=586.606, time_months=29.691, average_staff=19.767)
```

See `examples/` for a runnable script.
