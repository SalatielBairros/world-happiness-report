import pandas as pd
from lib.io_helper import create_directory_if_not_exists

class DatasetsJoin:
    """
    Esta é a quarta etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    Seu propósito é juntar o dataset com os dados até 2020 e o dataset com os dados de 2021, dado que ambos estão com as colunas normalizadas e idênticas.

    Attributes
    ----------
    base_directory : str
        Diretório base onde os datasets são armazenados e os modificados serão salvos.
    input_directory : str
        Diretório onde onde estão os datasets preparados para serem juntados.

    Methods
    -------
    execute()
        Executa o join dos datasets.
    
    """

    __name__ = 'DatasetsJoin'

    def __init__(self, base_directory='./data', input_directory='affects') -> None:
        self.base_directory = base_directory
        self.output_directory = f'{self.base_directory}/joined_dataset'
        self.input_directory = f'{self.base_directory}/{input_directory}'
        create_directory_if_not_exists(self.output_directory)

    def execute(self):
        past_data = pd.read_csv(self.input_directory + '/HistoricData.csv')
        data_2021 = pd.read_csv(self.input_directory + '/Data_2021.csv')

        data_2021['year'] = 2021

        columns = data_2021.columns
        past_data = past_data[columns]

        datasets = [past_data, data_2021]

        full_dataset = pd.concat(datasets)

        full_dataset.to_csv(self.output_directory + '/full_dataset.csv', index=False)