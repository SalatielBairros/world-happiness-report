import pandas as pd
from repository.local_storage_repository import LocalStorageRepository

class PandemicData:
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset
        self.repository = LocalStorageRepository()

    def execute(self):
        pandemic_countries = self.dataset.query("year == 2020")['cat_country'].unique()
        pandemic_coutries_data = self.dataset[self.dataset['cat_country'].isin(pandemic_countries)]
        self.repository.save_pandemic_countries_data(pandemic_coutries_data)
        return self.dataset

        