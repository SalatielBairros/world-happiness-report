from data_preparation.missing_data import MissingData
from data_preparation.region_cleaning import RegionCleaning
from data_preparation.commands_handler import Commands
from repository.local_storage_repository import LocalStorageRepository

def execute_data_preparation():
    repository = LocalStorageRepository()
    prepared_dataset = repository.get_prepared_dataset()
    if(prepared_dataset  is None):
        return Commands(repository) \
            .add_command(MissingData) \
            .add_command(RegionCleaning) \
            .execute()

    return prepared_dataset
