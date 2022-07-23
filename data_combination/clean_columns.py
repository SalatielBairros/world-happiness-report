import pandas as pd
from environment.constants import DatasetConstants

class CleanColumns:
    """
    Esta é a primeira etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    É composta por:

    1. Padronização da nomenclatura das colunas entre o dataset de dados histórios e dos dados de 2021.
    2. Exclusão das colunas do grupo "Explained by", visto que são presentes apenas no relatório de 2021 e não é relevante para os propósitos deste projeto
    3. Remoção de colunas com informações estatísticas: ['std_score', 'upperwhisker', 'lowerwhisker']    

    Attributes
    ----------
    past_data : pd.DataFrame
        Dados históricos
    data_2021 : pd.DataFrame
        Dados de 2021

    Methods
    -------
    execute()
        Executa a limpeza dos datasets de dados históricos e de dados de 2021.
    
    """
    
    __name__ = 'CleanColumns'

    def __init__(self, past_data: pd.DataFrame, data_2021: pd.DataFrame):        
        self.past_data = past_data
        self.data_2021 = data_2021


    def execute(self):        
        self.past_data.columns = DatasetConstants.PAST_DATA_COLUMNS

        self.data_2021 = self.data_2021[self.data_2021.columns[:12]]
        self.data_2021.columns = DatasetConstants.DATA_2021_COLUMNS
        self.data_2021.drop(columns=['std_score', 'upperwhisker', 'lowerwhisker'], inplace=True)

        return (self.past_data, self.data_2021)