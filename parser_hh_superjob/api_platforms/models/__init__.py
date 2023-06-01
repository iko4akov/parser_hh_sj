from parser_hh_superjob.api_platforms.models.hh_model import ModelHeadHunter
from parser_hh_superjob.api_platforms.models.superjob_model import ModelSuperJob

all_models = [
    ModelSuperJob.__class__,
    ModelHeadHunter.__class__
]
