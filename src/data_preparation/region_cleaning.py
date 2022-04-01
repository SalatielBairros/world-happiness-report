import pandas as pd
from lib.io_helper import create_directory_if_not_exists

class RegionCleaning:
    """
    Esta é a sexta etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    Ela realiza a atribuição das regiões utilizando um dataset externo e aplicando no dataset completo e tratado.
    É feita de forma separada ao `region_join`, pois esse tratamento busca apenas consolidar os dois datasets iniciais.
    Attributes
    ----------
    base_directory : str
        Diretório base onde o dataset resultante será salvo.
    input_directory : str
        Diretório onde o dataset completo do relatório se encontra.

    Methods
    -------
    execute()
        Executa a correção das regiões do mundo de cada país baseado no dataset externo.
    
    """
    
    __name__ = 'RegionCleaning'

    def __init__(self, base_directory = './data', input_directory='complete_dataset') -> None:
        self.base_directory = base_directory
        self.output_directory = f'{self.base_directory}/complete_dataset_region'
        self.input_directory = f'{self.base_directory}/{input_directory}'
        self.kaggle_directory = f'{self.base_directory}/kaggle'
        create_directory_if_not_exists(self.output_directory)

        self.regions_map = {
            'central and eastern europe': 'eastern europe',
            'southeast asia': 'asia (ex. near east)',
            'middle east and north africa': 'near east',
            'somaliland region': 'sub-saharan africa'
        }

    def get_db_countries(self):
        countries_usa_database = pd.read_csv(self.kaggle_directory + '/countries_usa_database.csv')

        countries = countries_usa_database[['Country', 'Region']].dropna()
        countries.columns = ['country', 'region']
        countries['region'] = countries['region'].str.split(',').str[0].str.split('(').str[0].str.strip().str.lower().str.replace('&', 'and')
        countries['country'] = countries['country'].str.split(',').str[0].str.split('(').str[0].str.strip().str.lower().str.replace('&', 'and').str.replace('rep.', 'republic', regex=False)
        countries.drop_duplicates(inplace=True)
        countries.set_index('country', inplace=True)
        return countries


    def get_region(self, country, region, db_countries):
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

    def execute(self):
        dataset = pd.read_csv('./data/complete_dataset/complete_dataset.csv')
        dataset['country'] = dataset['country'].str.split('(').str[0].str.strip()
        db_coutries = self.get_db_countries()
        for country in dataset.itertuples():    
            dataset.loc[country.Index, 'region'] = self.get_region(country.country, country.region, db_coutries)

        dataset.to_csv('./data/complete_dataset/complete_dataset_region.csv', index=False)