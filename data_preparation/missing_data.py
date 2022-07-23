import pandas as pd
import numpy as np

class MissingData:
    """
    Esta é a quinta etapa da preparação e limpeza iniciais dos dados do Relatório de Felicidade Mundial.
    Seu propósito é tratar os dados faltantes nos datasets baseado nas seguintes regras:

    1. Agrupa-se os dados faltantes de cada atributo por país
    2. Todos os países que, no total dos dados obtidos para aquele atributo ao longo do tempo, têm mais de 50% dos dados preenchidos, preenche os faltantes com a média dos anos mais próximos (anterior e posterior).
    3. Os países que tem 50% ou menos dos dados históricos para o atributo informados são preenchidos com o valor menor entre a média e a mediana mundial.

    Para que essas regras fossem estabelecidas foi realizada a análise de correlação e densidade dos dados faltantes.
    Essa análise pode ser obtida em analysis/MissingData.ipynb.

    Os datasets resultantes são salvos em uma pasta chamada 'complete_dataset' dentro da pasta do diretório informado no construtor.
    Attributes
    ----------
    dataset : pd.DataFrame
        Dataset para aplicar as transformações dos dados.    

    Methods
    -------
    execute()
        Execute o tratamento dos dados faltantes.
    
    """

    __name__ = 'MissingData'

    def __init__(self, dataset: pd.DataFrame) -> None:
        self.dataset = dataset

    def execute(self):
        att_with_na_values = list(self.dataset.columns[self.dataset.isnull().any()])

        for att in att_with_na_values:
            countries = self.get_countries_with_less_than_half_missing_data(att)
            self.fill_missing_data_with_closest_data_mean(att, countries)
            self.fill_missing_data_with_median_or_mean(att)

        return self.dataset

    def fill_missing_data_with_closest_data_mean(self, column_name, countries):
        df_countries = self.dataset[self.dataset['country'].isin(countries) & self.dataset[column_name].isna()][['country', 'year']]
        for country in df_countries.itertuples():
            before = self.dataset[(self.dataset['country'] == country.country) & (self.dataset['year'] < country.year)][[column_name, 'year']].sort_values(by='year', ascending=False)[column_name].values
            after = self.dataset[(self.dataset['country'] == country.country) & (self.dataset['year'] > country.year)][[column_name, 'year']].sort_values(by='year', ascending=False)[column_name].values
            
            total = []
            if(len(before) > 0):
                total.append(before[0])
            if(len(after) > 0):
                total.append(after[0])    

            self.dataset.loc[country.Index, column_name] = np.mean(total)        

    def fill_missing_data_with_median_or_mean(self, column_name):
        mean = self.dataset[column_name].mean()
        median = self.dataset[column_name].median()
        lower_value = min([mean, median])
        self.dataset[column_name].fillna(lower_value, inplace=True)        

    def get_countries_with_less_than_half_missing_data(self, column_name):
        missing_data_countries = self.dataset[self.dataset[column_name].isna()]['country'].unique()
        missing_data_countries_total = self.dataset[self.dataset['country'].isin(missing_data_countries)]['country'].value_counts()        
        by_country = pd.DataFrame([self.dataset[self.dataset[column_name].isna()]['country'].value_counts(), missing_data_countries_total]).T
        by_country.columns = ['total_missing_data', 'total_data']
        by_country['tx'] = (by_country['total_missing_data'] / by_country['total_data'])
        return list(by_country.query('tx < 0.5').index)
