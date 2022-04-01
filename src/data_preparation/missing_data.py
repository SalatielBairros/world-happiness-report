import pandas as pd
import numpy as np
from lib.io_helper import create_directory_if_not_exists

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
    base_directory : str
        Diretório base onde os datasets são armazenados e os modificados serão salvos.
    input_directory : str
        Diretório onde os datasets de origem estão armazenados. Os datasets de origem devem já estar com as colunas normalizadas.

    Methods
    -------
    execute()
        Execute o tratamento dos dados faltantes.
    
    """

    __name__ = 'MissingData'

    def __init__(self, base_directory='./data', input_directory='joined_dataset') -> None:
        self.base_directory = base_directory
        self.output_directory = f'{self.base_directory}/complete_dataset'
        self.input_directory = f'{self.base_directory}/{input_directory}'
        create_directory_if_not_exists(self.output_directory)

    def execute(self):
        dataset = pd.read_csv(self.input_directory + '/full_dataset.csv')
        att_with_na_values = list(dataset.columns[dataset.isnull().any()])

        for att in att_with_na_values:
            countries = self.get_countries_with_less_than_half_missing_data(dataset, att)
            dataset = self.fill_missing_data_with_closest_data_mean(dataset, att, countries)
            dataset = self.fill_missing_data_with_median_or_mean(dataset, att)

        dataset.to_csv(self.output_directory + '/complete_dataset.csv', index=False)

    def fill_missing_data_with_closest_data_mean(self, dataset, column_name, countries):
        df_countries = dataset[dataset['country'].isin(countries) & dataset[column_name].isna()][['country', 'year']]
        for country in df_countries.itertuples():
            before = dataset[(dataset['country'] == country.country) & (dataset['year'] < country.year)][[column_name, 'year']].sort_values(by='year', ascending=False)[column_name].values
            after = dataset[(dataset['country'] == country.country) & (dataset['year'] > country.year)][[column_name, 'year']].sort_values(by='year', ascending=False)[column_name].values
            
            total = []
            if(len(before) > 0):
                total.append(before[0])
            if(len(after) > 0):
                total.append(after[0])    

            dataset.loc[country.Index, column_name] = np.mean(total)
        return dataset    

    def fill_missing_data_with_median_or_mean(self, dataset, column_name):
        mean = dataset[column_name].mean()
        median = dataset[column_name].median()
        lower_value = min([mean, median])
        dataset[column_name].fillna(lower_value, inplace=True)
        return dataset

    def get_countries_with_less_than_half_missing_data(self, dataset, column_name):
        missing_data_countries = dataset[dataset[column_name].isna()]['country'].unique()
        missing_data_countries_total = dataset[dataset['country'].isin(missing_data_countries)]['country'].value_counts()        
        by_country = pd.DataFrame([dataset[dataset[column_name].isna()]['country'].value_counts(), missing_data_countries_total]).T
        by_country.columns = ['total_missing_data', 'total_data']
        by_country['tx'] = (by_country['total_missing_data'] / by_country['total_data'])
        return list(by_country.query('tx < 0.5').index)
