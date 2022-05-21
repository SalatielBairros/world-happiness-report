# from data_preparation.clean_columns import CleanColumns
from modeling.data_preparation.clean_columns import CleanColumns
# from data_preparation.region_join import RegionJoin
from modeling.data_preparation.region_join import RegionJoin
# from data_preparation.affects import Affects
from modeling.data_preparation.affects import Affects
# from data_preparation.dataset_join import DatasetsJoin
from modeling.data_preparation.dataset_join import DatasetsJoin
# from data_preparation.missing_data import MissingData
from modeling.data_preparation.missing_data import MissingData
# from data_preparation.region_cleaning import RegionCleaning
from modeling.data_preparation.region_cleaning import RegionCleaning
from lib.commands_handler import Commands

class DataPreparation():
    print('CHegueii')
    Commands() \
        .add_command(CleanColumns) \
        .add_command(RegionJoin) \
        .add_command(Affects) \
        .add_command(DatasetsJoin) \
        .add_command(MissingData) \
        .add_command(RegionCleaning) \
        .execute()


# command = GetFreeTimeCommand(id_person_apportionment)
# return command.execute()
