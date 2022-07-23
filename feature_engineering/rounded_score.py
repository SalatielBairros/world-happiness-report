import pandas as pd

class RoundedScore():
    __name__ = 'Rounded Score'

    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    def execute(self):        
        self.dataset['rounded_score'] = self.dataset['score'].round(0)
        return self.dataset