from data_combination.clean_columns import CleanColumns
from data_combination.region_join import RegionJoin
from data_combination.affects import Affects
from data_combination.commands_handler import Commands
from repository.local_storage_repository import LocalStorageRepository

def execute_data_combination():
    repository = LocalStorageRepository()
    joined_dataset = repository.get_joined_dataset()
    if(joined_dataset is None):
        return Commands(repository) \
            .add_command(CleanColumns) \
            .add_command(RegionJoin) \
            .add_command(Affects) \
            .execute_and_save()
    return joined_dataset
