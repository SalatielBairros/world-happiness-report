import pandas as pd
from lib.io_helper import create_directory_if_not_exists

class CleanColumns:
    """
    Esta é a primeira etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    É composta por:

    1. Padronização da nomenclatura das colunas entre o dataset de dados histórios e dos dados de 2021.
    2. Exclusão das colunas do grupo "Explained by", visto que são presentes apenas no relatório de 2021 e não é relevante para os propósitos deste projeto
    3. Remoção de colunas com informações estatísticas: ['std_score', 'upperwhisker', 'lowerwhisker']
    4. Exportação dos datasets editados para uma pasta chamada "cleaned_columns" 

    Attributes
    ----------
    base_directory : str
        Diretório base onde os datasets são armazenados e os modificados serão salvos.
    input_directory : str
        Diretório onde os datasets de dados históricos originais de 2021 serão armazenados.

    Methods
    -------
    execute()
        Executa a limpeza dos datasets de dados históricos e de dados de 2021.
    
    """

    def __init__(self, base_directory = './data', input_directory='original'):
        self.base_directory = base_directory
        self.input_directory = f'{self.base_directory}/{input_directory}'
        self.output_directory = f'{self.base_directory}/cleaned_columns'
        create_directory_if_not_exists(self.output_directory)

    def execute(self):
        past_data = pd.read_excel(self.input_directory + '/HistoricData.xls')
        past_data.columns = ['country', 'year', 'score', 'gdp', 'social_support', 'hle', 'freedom', 'generosity', 'corruption', 'positive_affect', 'negative_affect']
        past_data.to_csv(self.output_directory + '/HistoricData.csv', index=False)

        data_2021 = pd.read_excel(self.input_directory + '/Data_2021.xls')

        data_2021 = data_2021[data_2021.columns[:12]]
        data_2021.columns = ['country', 'region', 'score', 'std_score', 'upperwhisker', 'lowerwhisker', 'gdp', 'social_support', 'hle', 'freedom', 'generosity', 'corruption']
        data_2021.drop(columns=['std_score', 'upperwhisker', 'lowerwhisker'], inplace=True)
        data_2021.to_csv(self.output_directory + '/Data_2021.csv', index=False)