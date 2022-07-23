import pandas as pd

class CatRegion():
    __name__ = 'Cat Region'

    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset

    def execute(self):        
        self.dataset['cat_region'] = pd.Categorical(self.dataset['region'])
        self.dataset['cat_region'] = self.dataset['cat_region'].cat.codes
        return self.dataset        