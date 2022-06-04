from feature_engineering.cat_country import CatCountry
from feature_engineering.cat_region import CatRegion
from lib.commands_handler import Commands

Commands() \
    .add_command(CatRegion) \
    .add_command(CatCountry) \
    .execute()
