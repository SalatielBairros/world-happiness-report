import pandas as pd

class CatRegion():
    __name__ = 'Cat Region'

    def __init__(self, output_directory = './data/feature_engineering', input_file='./data/complete_dataset_region/complete_dataset_region.csv'):    
        self.output_directory = output_directory
        self.input_file = input_file

    def execute(self):
        dataset = pd.read_csv(self.input_file)
        dataset['cat_region'] = pd.Categorical(dataset['region'])
        dataset['cat_region'] = dataset['cat_region'].cat.codes
        dataset.to_csv(self.output_directory + '/cat_region.csv', index=False)