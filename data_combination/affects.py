import pandas as pd
from lib.io_helper import create_directory_if_not_exists

class Affects:
    """
    Esta é a terceira etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    Seu propósito é lidar com duas colunas ausentes nos dados de 2021 mas presentes nos dados históricos: positive_affects e negative_affects.
    Ambos os atributos são responsáveis por quantificar o estado sentimental das pessoas de determinado país. 
    Para isso é perguntado ao entrevistado a presença de afetos positivos como alegria, apreciação e sorrisos, assim como de sentimentos negativos como preocupação, tristeza e raiva.
    Como os dados ausentess são apenas do último ano, a decisão tomada foi repetir o valor do último ano em que a pesquisa obteve os valores para cada país.

    Attributes
    ----------
    past_data : pd.DataFrame
        Dados históricos
    data_2021 : pd.DataFrame
        Dados de 2021

    Methods
    -------
    execute()
        Executa a preparação dos dados.
    
    """

    __name__ = 'Affects'

    def __init__(self, past_data: pd.DataFrame, data_2021: pd.DataFrame) -> None:
        self.past_data = past_data
        self.data_2021 = data_2021
        self.retroactive_positive_affects = []
        self.retroactive_negative_affects = []        

    def get_affects_by_year_and_country(self):
        past_data_affects = self.past_data[[
            'country', 'positive_affect', 'negative_affect', 'year']].copy()
        data_2020_affects = past_data_affects.query("year == 2020")
        data_2020_positive_affects = data_2020_affects[['country', 'positive_affect']].set_index(
            'country').to_dict('dict')['positive_affect']
        data_2020_negative_affects = data_2020_affects[['country', 'negative_affect']].set_index(
            'country').to_dict('dict')['negative_affect']

        data_2019_affects = past_data_affects.query("year == 2019")
        data_2019_positive_affects = data_2019_affects[['country', 'positive_affect']].set_index(
            'country').to_dict('dict')['positive_affect']
        data_2019_negative_affects = data_2019_affects[['country', 'negative_affect']].set_index(
            'country').to_dict('dict')['negative_affect']

        data_2018_affects = past_data_affects.query("year == 2018")
        data_2018_positive_affects = data_2018_affects[['country', 'positive_affect']].set_index(
            'country').to_dict('dict')['positive_affect']
        data_2018_negative_affects = data_2018_affects[['country', 'negative_affect']].set_index(
            'country').to_dict('dict')['negative_affect']

        self.retroactive_positive_affects = [
            data_2020_positive_affects, data_2019_positive_affects, data_2018_positive_affects]
        self.retroactive_negative_affects = [
            data_2020_negative_affects, data_2019_negative_affects, data_2018_negative_affects]

    def get_positive_affects(self, country):
        for year_affetcs in self.retroactive_positive_affects:
            if(country in year_affetcs):
                return year_affetcs[country]
        return 0

    def get_negative_affects(self, country):
        for year_affetcs in self.retroactive_negative_affects:
            if(country in year_affetcs):
                return year_affetcs[country]
        return 0

    def execute(self):
        self.get_affects_by_year_and_country()

        self.data_2021['positive_affect'] = self.data_2021['country'].apply(self.get_positive_affects)
        self.data_2021['negative_affect'] = self.data_2021['country'].apply(self.get_negative_affects)

        return (self.past_data, self.data_2021)
        