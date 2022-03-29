from data_preparation.clean_columns import CleanColumns
from data_preparation.region import Region
from data_preparation.affects import Affects
from data_preparation.dataset_join import DatasetsJoin
from data_preparation.missing_data import MissingData
from lib.commands_handler import Commands

Commands() \
    .add_command(CleanColumns) \
    .add_command(Region) \
    .add_command(Affects) \
    .add_command(DatasetsJoin) \
    .add_command(MissingData) \
    .execute()
    