import sys
from pathlib import Path
parent_name = Path('./').resolve().name
sys.path.append(f'../{parent_name}/src/lib')

import pandas as pd
from io_helper import create_directory_if_not_exists

base_directory = './data'
output_directory = f'{base_directory}/with_region'
input_directory = f'{base_directory}/cleaned_columns'
kaggle_directory = f'{base_directory}/kaggle'
create_directory_if_not_exists(output_directory)

past_data = pd.read_csv(input_directory + '/HistoricData.csv')
data_2021 = pd.read_csv(input_directory + '/Data_2021.csv')
kaggle_2015 = pd.read_csv(kaggle_directory + '/2015.csv')
kaggle_2016 = pd.read_csv(kaggle_directory + '/2016.csv')

df_regions = data_2021[['country', 'region']].copy()
df_regions['country'] = list(df_regions['country'].str.lower())
df_regions['region'] = list(df_regions['region'].str.lower())
regions = df_regions.set_index('country').to_dict('dict')['region']

df_kaggle_regions = kaggle_2015[['Country', 'Region']].copy()
df_kaggle_regions['Country'] = list(df_kaggle_regions['Country'].str.lower())
df_kaggle_regions['Region'] = list(df_kaggle_regions['Country'].str.lower())
kaggle_regions = df_kaggle_regions.set_index('Country').to_dict('dict')['Region']

df_kaggle_2016_regions = kaggle_2016[['Country', 'Region']].copy()
df_kaggle_2016_regions['Country'] = list(df_kaggle_2016_regions['Country'].str.lower())
df_kaggle_2016_regions['Region'] = list(df_kaggle_2016_regions['Country'].str.lower())
kaggle_2016_regions = df_kaggle_2016_regions.set_index('Country').to_dict('dict')['Region']

def get_region(country):
    if(country.lower() in regions):
        return regions[country.lower()]
    elif(country.lower() in kaggle_regions):
        return kaggle_regions[country.lower()]
    elif(country.lower() in kaggle_2016_regions):
        return kaggle_2016_regions[country.lower()]
    elif(country.lower() in ['cuba', 'guyana']):
        return 'Latin America and Caribbean'
    return 'Other' 

past_data['region'] = past_data['country'].apply(get_region)

past_data['country'] = list(past_data['country'].str.lower())
data_2021['country'] = list(data_2021['country'].str.lower())
data_2021['region'] = list(data_2021['region'].str.lower())

past_data.to_csv(output_directory + '/HistoricData.csv', index=False)
data_2021.to_csv(output_directory + '/Data_2021.csv', index=False)