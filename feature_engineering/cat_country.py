import pandas as pd

class CatCountry():
    __name__ = 'Cat Country'

    def __init__(self, dataset: pd.DataFrame):    
        self.dataset = dataset

    def execute(self):        
        self.dataset['cat_country'] = pd.Categorical(self.dataset['country'])
        self.dataset['cat_country'] = self.dataset['cat_country'].cat.codes
        return self.dataset