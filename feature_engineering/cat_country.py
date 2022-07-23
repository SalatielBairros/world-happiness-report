import pandas as pd

class CatCountry():
    __name__ = 'Cat Country'

    def __init__(self, output_directory = './data/feature_engineering', input_file='./data/feature_engineering/cat_region.csv'):    
        self.output_directory = output_directory
        self.input_file = input_file

    def execute(self):
        dataset = pd.read_csv(self.input_file)
        dataset['cat_country'] = pd.Categorical(dataset['country'])
        dataset['cat_country'] = dataset['cat_country'].cat.codes
        dataset.to_csv(self.output_directory + '/cat_country.csv', index=False)