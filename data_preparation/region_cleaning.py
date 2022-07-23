import pandas as pd
from services.region_service import RegionService


class RegionCleaning:
    """
    Esta é a sexta etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    Ela realiza a atribuição das regiões utilizando um dataset externo e aplicando no dataset completo e tratado.
    É feita de forma separada ao `region_join`, pois esse tratamento busca apenas consolidar os dois datasets iniciais.
    Attributes
    ----------
    dataset : pd.DataFrame
        Dataset para o processamento
    
    Methods
    -------
    execute()
        Executa a correção das regiões do mundo de cada país baseado no dataset externo.

    """

    __name__ = 'RegionCleaning'

    def __init__(self, dataset: pd.DataFrame) -> None:
        self.region_service = RegionService()
        self.dataset = dataset

    def execute(self) -> pd.DataFrame:
        self.dataset['country'] = self.dataset['country'].str.split('(').str[0].str.strip()
        
        for country in self.dataset.itertuples():
            self.dataset.loc[country.Index, 'region'] = self.region_service.get_region(country.country, country.region)

        return self.dataset
