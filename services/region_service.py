import pandas as pd
from os import path
from lib.memo_cache import memo

class RegionService:
    def __init__(self):
        self.kaggle_region_dataset = './data/processed/kaggle_region_datasets.csv'

        self.regions_map = {
            'central and eastern europe': 'eastern europe',
            'southeast asia': 'asia',
            'middle east and north africa': 'near east',
            'somaliland region': 'sub-saharan africa'
        }

    def __merge_kaggle_datasets__(self):
        df_2015 = pd.read_csv('./data/original/kaggle_2015.csv')[['Country', 'Region']]
        df_2016 = pd.read_csv('./data/original/kaggle_2016.csv')[['Country', 'Region']]
        kaggle_region_datasets = df_2015.append(df_2016, ignore_index=True)
        kaggle_region_datasets = kaggle_region_datasets.groupby('Country').first().reset_index()
        kaggle_region_datasets.to_csv(self.kaggle_region_dataset, index=False)
        return kaggle_region_datasets

    def get_kaggle_regions(self) -> pd.DataFrame:
        if(path.exists(self.kaggle_region_dataset)):
            return pd.read_csv(self.kaggle_region_dataset)

        if(self.__exists_kaggle_region_datasets__()):
            return self.__merge_kaggle_datasets__()

        return None

    def __exists_kaggle_region_datasets__(self):
        return path.exists('./data/original/kaggle_2015.csv') and path.exists('./data/original/kaggle_2016.csv')

    @memo
    def get_db_countries(self):
        countries_usa_database = pd.read_csv('./data/original/countries_usa_database.csv')

        countries = countries_usa_database[['Country', 'Region']].dropna()
        countries.columns = ['country', 'region']
        
        countries['region'] = countries['region'].str.split(',').str[0].str.split(
            '(').str[0].str.strip().str.lower().str.replace('&', 'and')

        countries['country'] = countries['country'].str.split(',').str[0].str.split(
            '(').str[0].str.strip().str.lower().str.replace('&', 'and').str.replace('rep.', 'republic', regex=False)

        countries.drop_duplicates(inplace=True)
        countries.set_index('country', inplace=True)
        return countries

    
    def get_region(self, country: str, region: str):
        db_countries = self.get_db_countries()

        regions = db_countries['region']
        if(region in list(regions)):
            return region
        if(country in db_countries.index):
            return regions[country]
        for uc in db_countries.index:
            if(country.startswith(uc)):
                return regions[uc]
            if(uc in country.split(' ')):
                return regions[uc]
        if(region in self.regions_map):
            return self.regions_map[region]

        return 'Other'
