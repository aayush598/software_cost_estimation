from software_cost_estimation import CocomoIIModel
from software_cost_estimation.core.types import EstimationInput

def test_nominal_case():
    scale = {key: "N" for key in CocomoIIModel.required_rating_keys()["scale_factors"]}
    em = {key: "N" for key in CocomoIIModel.required_rating_keys()["effort_multipliers"]}
    model = CocomoIIModel()
    result = model(EstimationInput(size_ksloc=100.0, scale_factors=scale, effort_multipliers=em))

    assert round(result.person_months, 1) == 465.3
    assert round(result.time_months, 1) == 25.9
    assert round(result.avg_staff, 1) == 18.0
