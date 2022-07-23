import logging
from os import environ as env, path
from environment.constants import EnvironmentVariables
import wget
from data_combination.data_combination_commands import execute_data_combination
from data_preparation.data_preparation_commands import execute_data_preparation
from feature_engineering.feature_engineering_commands import execute_feature_engineering
import pandas as pd
from lib.io_helper import create_directory_if_not_exists

class WhrDataIngestion:
    def __init__(self):        
        self.__create_directories__()
        self.original_path = './data/original'

    def ingest(self) -> pd.DataFrame:
        self.download_data() 
        _ = execute_data_combination()
        _ = execute_data_preparation()
        return execute_feature_engineering()

    def download_data(self):
        historic_data_url = env[EnvironmentVariables.ORIGINAL_HISTORIC_DATA_URL]
        data_2021_url = env[EnvironmentVariables.DATA_2021_URL]
        kaggle_regions_url = env[EnvironmentVariables.KAGGLE_REGIONS]

        historic_data_filename = "HistoricData.xls"
        data_2021_filename = "Data_2021.xls"

        if(not self.__has_ingested_file__(historic_data_filename)):
            logging.info("Ingesting historic data...")
            wget.download(historic_data_url, f'{self.original_path}/{historic_data_filename}')

        if(not self.__has_ingested_file__(data_2021_filename)):
            logging.info("Ingesting 2021 data...")
            wget.download(data_2021_url, f'{self.original_path}/{data_2021_filename}')

        if(not path.exists('./data/reference/kaggle_region_datasets.csv')):
            logging.info("Ingesting Kaggle Regions...")
            wget.download(kaggle_regions_url, './data/reference/kaggle_region_datasets.csv')

    def __has_ingested_file__(self, filename: str):
        return path.exists(f'./data/original/{filename}')

    def __create_directories__(self):
        create_directory_if_not_exists('./data')
        create_directory_if_not_exists('./data/original')
        create_directory_if_not_exists('./data/reference')
