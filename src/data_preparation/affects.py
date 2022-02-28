import sys
from pathlib import Path
parent_name = Path('./').resolve().name
sys.path.append(f'../{parent_name}/src/lib')

import pandas as pd
from io_helper import create_directory_if_not_exists

base_directory = './data'
output_directory = f'{base_directory}/affects'
input_directory = f'{base_directory}/with_region'
create_directory_if_not_exists(output_directory)

past_data = pd.read_csv(input_directory + '/HistoricData.csv')
data_2021 = pd.read_csv(input_directory + '/Data_2021.csv')

past_data_affects = past_data[['country', 'positive_affect', 'negative_affect', 'year']].copy()
data_2020_affects = past_data_affects.query("year == 2020")
data_2020_positive_affects = data_2020_affects[['country', 'positive_affect']].set_index('country').to_dict('dict')['positive_affect']
data_2020_negative_affects = data_2020_affects[['country', 'negative_affect']].set_index('country').to_dict('dict')['negative_affect']

data_2019_affects = past_data_affects.query("year == 2019")
data_2019_positive_affects = data_2019_affects[['country', 'positive_affect']].set_index('country').to_dict('dict')['positive_affect']
data_2019_negative_affects = data_2019_affects[['country', 'negative_affect']].set_index('country').to_dict('dict')['negative_affect']

data_2018_affects = past_data_affects.query("year == 2018")
data_2018_positive_affects = data_2018_affects[['country', 'positive_affect']].set_index('country').to_dict('dict')['positive_affect']
data_2018_negative_affects = data_2018_affects[['country', 'negative_affect']].set_index('country').to_dict('dict')['negative_affect']


def get_last_positive_affect(country):
    if(country in data_2020_positive_affects):
        return data_2020_positive_affects[country]
    elif(country in data_2019_positive_affects):
        return data_2019_positive_affects[country]
    elif(country in data_2018_positive_affects):
        return data_2018_positive_affects[country]
    return 0

def get_last_negative_affect(country):
    if(country in data_2020_negative_affects):
        return data_2020_negative_affects[country]
    elif(country in data_2019_negative_affects):
        return data_2019_negative_affects[country]
    elif(country in data_2018_negative_affects):
        return data_2018_negative_affects[country]
    return 0

data_2021['positive_affect'] = data_2021['country'].apply(get_last_positive_affect)
data_2021['negative_affect'] = data_2021['country'].apply(get_last_negative_affect)

past_data.to_csv(output_directory + '/HistoricData.csv', index=False)
data_2021.to_csv(output_directory + '/Data_2021.csv', index=False)