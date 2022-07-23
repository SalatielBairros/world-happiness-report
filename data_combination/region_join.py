import pandas as pd
from services.region_service import RegionService

class RegionJoin:
    """
    Esta é a segunda etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    Ela é necessária pois apenas os dados de 2021 são preenchidos com a região no mundo em que um país se encontra. 
    Para resolver isso foi realizado o preenchimento dos dados históricos baseado na região informada nos dados do ano de 2021.
    Contudo, nem todos os países do mundo possuem a informação de região no ano de 2021. 
    Para resolver isso foram utilizadas bases do Kaggle de 2015 e 2016 que continham esses dados.    

    Attributes
    ----------
    past_data : pd.DataFrame
        Dados históricos
    data_2021 : pd.DataFrame
        Dados de 2021
        
    Methods
    -------
    execute()
        Executa o preenchimento das regiões dos países no mundo no dataset de dados históricos.
    
    """

    __name__ = 'RegionJoin'

    def __init__(self, past_data: pd.DataFrame, data_2021: pd.DataFrame) -> None:
        self.past_data = past_data
        self.data_2021 = data_2021
        
    def get_region_datasets(self):        
        kaggle_datasets =  RegionService().get_kaggle_regions()
        
        df_regions = self.data_2021[['country', 'region']].copy()
        df_regions['country'] = list(df_regions['country'].str.lower())
        df_regions['region'] = list(df_regions['region'].str.lower())
        regions = df_regions.set_index('country').to_dict('dict')['region']

        df_kaggle_regions = kaggle_datasets[['Country', 'Region']].copy()
        df_kaggle_regions['Country'] = list(df_kaggle_regions['Country'].str.lower())
        df_kaggle_regions['Region'] = list(df_kaggle_regions['Country'].str.lower())
        kaggle_regions = df_kaggle_regions.set_index('Country').to_dict('dict')['Region']        

        return [regions, kaggle_regions]

    def get_region(self, country):
        if(country.lower() in ['cuba', 'guyana']):
            return 'Latin America and Caribbean'       

        for regions in self.get_region_datasets():
            if(country.lower() in regions):
                return regions[country.lower()]
        
        return 'Other' 

    def execute(self):
        self.past_data['region'] = self.past_data['country'].apply(self.get_region)
        self.past_data['country'] = list(self.past_data['country'].str.lower())
        self.data_2021['country'] = list(self.data_2021['country'].str.lower())
        self.data_2021['region'] = list(self.data_2021['region'].str.lower())

        return (self.past_data, self.data_2021)