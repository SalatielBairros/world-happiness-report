import logging
from os import environ as env, path
from environment.constants import EnvironmentVariables
import wget
from data_combination.data_combination_commands import execute_data_combination
from data_preparation.data_preparation_commands import execute_data_preparation
from feature_engineering.feature_engineering_commands import execute_feature_engineering
from data_augmentation.data_augmentation_executor import execute_data_augmentation
from lib.io_helper import create_directory_if_not_exists

class WhrDataIngestion:
    def __init__(self):        
        self.__create_directories__()
        self.original_path = './data/original'

    def ingest(self) -> None:
        self.download_data() 
        _ = execute_data_combination()
        _ = execute_data_preparation()
        _ = execute_feature_engineering()
        _ = execute_data_augmentation()

    def download_data(self):
        urls = [env[env_url_var] for env_url_var in EnvironmentVariables.ORIGINAL_URLS]

        for url in urls:
            filename = url.split('/')[-1]
            if(not self.__has_ingested_file__(filename)):
                logging.info(f"Ingesting {filename}...")
                wget.download(url, f'{self.original_path}/{filename}')
                logging.info(f"Ingested {filename}")

    def __has_ingested_file__(self, filename: str):
        return path.exists(f'./data/original/{filename}')

    def __create_directories__(self):
        create_directory_if_not_exists('./data')
        create_directory_if_not_exists('./data/original')
