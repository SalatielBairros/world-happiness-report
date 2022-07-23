import pandas as pd
class DatasetsJoin:
    """
    Esta é a quarta etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    Seu propósito é juntar o dataset com os dados até 2020 e o dataset com os dados de 2021, dado que ambos estão com as colunas normalizadas e idênticas.

    Attributes
    ----------
    past_data : pd.DataFrame
        Dados históricos
    data_2021 : pd.DataFrame
        Dados de 2021

    Methods
    -------
    execute()
        Executa o join dos datasets.
    
    """

    __name__ = 'DatasetsJoin'

    def __init__(self, past_data: pd.DataFrame, data_2021: pd.DataFrame) -> None:
        self.past_data = past_data
        self.data_2021 = data_2021

    def execute(self):
        self.data_2021['year'] = 2021

        columns = self.data_2021.columns
        self.past_data = self.past_data[columns]

        datasets = [self.past_data, self.data_2021]

        full_dataset = pd.concat(datasets)
        return full_dataset