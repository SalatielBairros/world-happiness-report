import pandas as pd
from os import path
from lib.io_helper import create_directory_if_not_exists

class LocalStorageRepository:
    def __init__(self) -> None:
        self.__create_directories__()
        self.joined_datasets_path = './data/processed/joined_dataset.csv'
        self.prepared_datasets_path = './data/processed/prepared_dataset.csv'
        self.processed_datasets_path = './data/processed/processed_dataset.csv'
        self.validation_datasets_path = './data/processed/validation_dataset.csv'
        self.augmented_datasets_path = './data/processed/augmented_dataset.csv'
        self.full_augmented_datasets_path = './data/processed/full_augmented_dataset.csv'
        self.pandemic_countries_data_path = './data/processed/pandemic_countries_dataset.csv'        

    def get_original_historic_data(self) -> pd.DataFrame:
        return pd.read_excel('./data/original/HistoricData.xls')

    def get_original_2021_data(self) -> pd.DataFrame:
        return pd.read_excel('./data/original/Data_2021.xls')

    def save_joined_dataset(self, dataset: pd.DataFrame):
        dataset.to_csv(self.joined_datasets_path, index=False)

    def save_prepared_dataset(self, dataset: pd.DataFrame):
        dataset.to_csv(self.prepared_datasets_path, index=False)

    def save_processed_dataset(self, dataset: pd.DataFrame):
        dataset.to_csv(self.processed_datasets_path, index=False)

    def save_validation_dataset(self, dataset: pd.DataFrame):
        dataset.to_csv(self.validation_datasets_path, index=False)

    def save_augmented_dataset(self, dataset: pd.DataFrame):
        dataset.to_csv(self.augmented_datasets_path, index=False)

    def save_full_augmented_dataset(self, dataset: pd.DataFrame):
        dataset.to_csv(self.full_augmented_datasets_path, index=False)

    def save_pandemic_countries_data(self, dataset: pd.DataFrame):
        dataset.to_csv(self.pandemic_countries_data_path, index=False)

    def get_joined_dataset(self) -> pd.DataFrame:
        if(path.exists(self.joined_datasets_path)):
            return pd.read_csv(self.joined_datasets_path)
        return None

    def get_prepared_dataset(self) -> pd.DataFrame:
        if(path.exists(self.prepared_datasets_path)):
            return pd.read_csv(self.prepared_datasets_path)
        return None

    def get_processed_dataset(self) -> pd.DataFrame:
        if(path.exists(self.processed_datasets_path)):
            return pd.read_csv(self.processed_datasets_path)
        return None

    def get_validation_dataset(self) -> pd.DataFrame:
        if(path.exists(self.validation_datasets_path)):
            return pd.read_csv(self.validation_datasets_path)
        return None
        
    def get_augmented_dataset(self) -> pd.DataFrame:
        if(path.exists(self.augmented_datasets_path)):
            return pd.read_csv(self.augmented_datasets_path)
        return None        

    def get_full_augmented_dataset(self) -> pd.DataFrame:
        if(path.exists(self.full_augmented_datasets_path)):
            return pd.read_csv(self.full_augmented_datasets_path)
        return None        

    def __create_directories__(self):
        create_directory_if_not_exists('./data')
        create_directory_if_not_exists('./data/original')
        create_directory_if_not_exists('./data/processed')