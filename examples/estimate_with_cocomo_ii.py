"""Example console script demonstrating how to call the library."""

from software_cost_estimation import CocomoIIModel
from software_cost_estimation.core.types import EstimationInput

scale = {
    "PREC": "N",
    "FLEX": "N",
    "RESL": "N",
    "TEAM": "N",
    "PMAT": "N",
}

em = {
    "RELY": "N",
    "DATA": "N",
    "CPLX": "N",
    "RUSE": "N",
    "DOCU": "N",
    "TIME": "N",
    "STOR": "N",
    "PVOL": "N",
    "ACAP": "N",
    "PCAP": "N",
    "APEX": "N",
    "PLEX": "N",
    "LTEX": "N",
    "TOOL": "N",
    "SITE": "N",
    "SCED": "N",
}

model = CocomoIIModel()
inputs = EstimationInput(size_ksloc=100.0, scale_factors=scale, effort_multipliers=em)
res = model(inputs)
print(res.as_dict())
