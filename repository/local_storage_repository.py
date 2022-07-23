import pandas as pd
from os import path
from lib.io_helper import create_directory_if_not_exists

class LocalStorageRepository:
    def __init__(self) -> None:
        self.__create_directories__()
        self.joined_datasets_path = './data/processed/joined_dataset.csv'

    def get_original_historic_data(self) -> pd.DataFrame:
        return pd.read_excel('./data/original/HistoricData.xls')

    def get_original_2021_data(self) -> pd.DataFrame:
        return pd.read_excel('./data/original/Data_2021.xls')

    def save_joined_dataset(self, dataset: pd.DataFrame):
        dataset.to_csv(self.joined_datasets_path, index=False)

    def get_joined_dataset(self) -> pd.DataFrame:
        if(path.exists(self.joined_datasets_path)):
            return pd.read_csv(self.joined_datasets_path)
        return None

    def __create_directories__(self):
        create_directory_if_not_exists('./data')
        create_directory_if_not_exists('./data/original')
        create_directory_if_not_exists('./data/processed')