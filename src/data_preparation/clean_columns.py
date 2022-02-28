import sys
from pathlib import Path
parent_name = Path('./').resolve().name
sys.path.append(f'../{parent_name}/src/lib')

import pandas as pd
from io_helper import create_directory_if_not_exists

base_directory = './data'
output_directory = f'{base_directory}/cleaned_columns'
input_directory = f'{base_directory}/original'
create_directory_if_not_exists(output_directory)

past_data = pd.read_excel(input_directory + '/HistoricData.xls')
past_data.columns = ['country', 'year', 'score', 'gdp', 'social_support', 'hle', 'freedom', 'generosity', 'corruption', 'positive_affect', 'negative_affect']
past_data.to_csv(output_directory + '/HistoricData.csv', index=False)

data_2021 = pd.read_excel(input_directory + '/Data_2021.xls')
# Removing "Explained by" columns
data_2021 = data_2021[data_2021.columns[:12]]
data_2021.columns = ['country', 'region', 'score', 'std_score', 'upperwhisker', 'lowerwhisker', 'gdp', 'social_support', 'hle', 'freedom', 'generosity', 'corruption']
data_2021.drop(columns=['std_score', 'upperwhisker', 'lowerwhisker'], inplace=True)
data_2021.to_csv(output_directory + '/Data_2021.csv', index=False)