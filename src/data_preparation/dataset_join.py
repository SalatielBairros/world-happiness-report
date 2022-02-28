import sys
from pathlib import Path
parent_name = Path('./').resolve().name
sys.path.append(f'../{parent_name}/src/lib')

import pandas as pd
from io_helper import create_directory_if_not_exists

base_directory = './data'
output_directory = f'{base_directory}/joined_dataset'
input_directory = f'{base_directory}/affects'
create_directory_if_not_exists(output_directory)

past_data = pd.read_csv(input_directory + '/HistoricData.csv')
data_2021 = pd.read_csv(input_directory + '/Data_2021.csv')

data_2021['year'] = 2021

columns = data_2021.columns
past_data = past_data[columns]

datasets = [past_data, data_2021]

full_dataset = pd.concat(datasets)

full_dataset.to_csv(output_directory + '/full_dataset.csv', index=False)