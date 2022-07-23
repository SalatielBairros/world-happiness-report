import pandas as pd
from lib.io_helper import create_directory_if_not_exists

class RegionJoin:
    """
    Esta é a segunda etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    Ela é necessária pois apenas os dados de 2021 são preenchidos com a região no mundo em que um país se encontra. 
    Para resolver isso foi realizado o preenchimento dos dados históricos baseado na região informada nos dados do ano de 2021.
    Contudo, nem todos os países do mundo possuem a informação de região no ano de 2021. 
    Para resolver isso foram utilizadas bases do Kaggle de 2015 e 2016 que continham esses dados.
    Os datasets resultantes são salvos em uma pasta chamada 'with_region' dentro da pasta do diretório informado no construtor.
    Attributes
    ----------
    base_directory : str
        Diretório base onde os datasets são armazenados e os modificados serão salvos.
    input_directory : str
        Diretório onde os datasets de origem estão armazenados. Os datasets de origem devem já estar com as colunas normalizadas.

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
        data_2021 = pd.read_csv(self.input_directory + '/Data_2021.csv')
        kaggle_2015 = pd.read_csv(self.kaggle_directory + '/2015.csv')
        kaggle_2016 = pd.read_csv(self.kaggle_directory + '/2016.csv')

        df_regions = data_2021[['country', 'region']].copy()
        df_regions['country'] = list(df_regions['country'].str.lower())
        df_regions['region'] = list(df_regions['region'].str.lower())
        regions = df_regions.set_index('country').to_dict('dict')['region']

        df_kaggle_regions = kaggle_2015[['Country', 'Region']].copy()
        df_kaggle_regions['Country'] = list(df_kaggle_regions['Country'].str.lower())
        df_kaggle_regions['Region'] = list(df_kaggle_regions['Country'].str.lower())
        kaggle_2015_regions = df_kaggle_regions.set_index('Country').to_dict('dict')['Region']

        df_kaggle_2016_regions = kaggle_2016[['Country', 'Region']].copy()
        df_kaggle_2016_regions['Country'] = list(df_kaggle_2016_regions['Country'].str.lower())
        df_kaggle_2016_regions['Region'] = list(df_kaggle_2016_regions['Country'].str.lower())
        kaggle_2016_regions = df_kaggle_2016_regions.set_index('Country').to_dict('dict')['Region']

        return [regions, kaggle_2015_regions, kaggle_2016_regions]

    def get_region(self, country):
        if(country.lower() in ['cuba', 'guyana']):
            return 'Latin America and Caribbean'       

        for regions in self.get_region_datasets():
            if(country.lower() in regions):
                return regions[country.lower()]
        
        return 'Other' 

    def execute(self):
        past_data = pd.read_csv(self.input_directory + '/HistoricData.csv')
        data_2021 = pd.read_csv(self.input_directory + '/Data_2021.csv')

        past_data['region'] = past_data['country'].apply(self.get_region)

        past_data['country'] = list(past_data['country'].str.lower())
        data_2021['country'] = list(data_2021['country'].str.lower())
        data_2021['region'] = list(data_2021['region'].str.lower())

        past_data.to_csv(self.output_directory + '/HistoricData.csv', index=False)
        data_2021.to_csv(self.output_directory + '/Data_2021.csv', index=False)