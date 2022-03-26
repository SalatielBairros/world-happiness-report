from data_preparation.clean_columns import CleanColumns
from data_preparation.region import Region
from data_preparation.affects import Affects
from data_preparation.dataset_join import DatasetsJoin

CleanColumns().execute()
Region().execute()
Affects().execute()
DatasetsJoin().execute()