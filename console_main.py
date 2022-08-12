import pandas as pd
import pickle

dataset = pd.read_csv('./data/processed/joined_dataset.csv').reset_index().sort_values(by='region').rename(columns={'index': 'custom_index'}).set_index('custom_index')
print(dataset)
dataset_copy = pickle.loads(pickle.dumps(dataset))
print(dataset)