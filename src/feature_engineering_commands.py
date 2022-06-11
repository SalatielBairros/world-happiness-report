from feature_engineering.cat_country import CatCountry
from feature_engineering.cat_region import CatRegion
from feature_engineering.rounded_score import RoundedScore
from feature_engineering.scaled_hle import ScaledHle
from lib.commands_handler import Commands

Commands() \
    .add_command(CatRegion) \
    .add_command(CatCountry) \
    .add_command(RoundedScore) \
    .add_command(ScaledHle) \
    .execute()
