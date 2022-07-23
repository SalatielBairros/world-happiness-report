import pandas as pd
from os import path

class RegionService:
    def __init__(self):
        self.kaggle_region_dataset = './data/reference/region/kaggle_region_datasets.csv'

    def merge_kaggle_datasets(self):
        if(path.exists(self.kaggle_region_dataset)):
            return pd.read_csv(self.kaggle_region_dataset)
            
        df_2015 = pd.read_csv('./data/reference/region/kaggle_2015.csv')[['Country', 'Region']]
        df_2016 = pd.read_csv('./data/reference/region/kaggle_2016.csv')[['Country', 'Region']]
        kaggle_region_datasets = df_2015.append(df_2016, ignore_index=True)
        kaggle_region_datasets = kaggle_region_datasets.groupby('Country').first().reset_index()
        kaggle_region_datasets.to_csv(self.kaggle_region_dataset, index=False)
        return kaggle_region_datasets
