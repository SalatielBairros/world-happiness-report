from data_combination.clean_columns import CleanColumns
from data_combination.region_join import RegionJoin
from data_combination.affects import Affects
from data_combination.dataset_join import DatasetsJoin
from data_preparation.missing_data import MissingData
from data_preparation.region_cleaning import RegionCleaning
from lib.commands_handler import Commands

Commands() \
    .add_command(CleanColumns) \
    .add_command(RegionJoin) \
    .add_command(Affects) \
    .add_command(DatasetsJoin) \
    .add_command(MissingData) \
    .add_command(RegionCleaning) \
    .execute()
