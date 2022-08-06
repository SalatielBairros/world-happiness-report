from feature_engineering.cat_country import CatCountry
from feature_engineering.cat_region import CatRegion
from feature_engineering.rounded_score import RoundedScore
from feature_engineering.scaled_hle import ScaledHle
from feature_engineering.pandemic_data import PandemicData
from feature_engineering.commands_handler import Commands
from repository.local_storage_repository import LocalStorageRepository

def execute_feature_engineering():
    repository = LocalStorageRepository()
    processed_dataset = repository.get_processed_dataset()
    if(processed_dataset is None):
        return Commands(repository) \
            .add_command(CatRegion) \
            .add_command(CatCountry) \
            .add_command(RoundedScore) \
            .add_command(ScaledHle) \
            .add_command(PandemicData) \
            .execute_and_save()
    return processed_dataset


