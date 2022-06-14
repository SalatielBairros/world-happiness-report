import pandas as pd

class RoundedScore():
    __name__ = 'Rounded Score'

    def __init__(self, output_directory = './data/feature_engineering', input_file='./data/feature_engineering/cat_country.csv'):    
        self.output_directory = output_directory
        self.input_file = input_file

    def execute(self):
        dataset = pd.read_csv(self.input_file)
        dataset['rounded_score'] = dataset['score'].round(0)        
        dataset.to_csv(self.output_directory + '/rounded_score.csv', index=False)