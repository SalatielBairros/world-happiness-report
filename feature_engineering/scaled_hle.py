import pandas as pd

class ScaledHle():
    """
    Com o propósito de melhorar a visualização dos dados, cria uma escala de HLE entre 0 e 1 utilizando o MinMaxScaler.
    No entanto é utilizado um intervalo customizado, 
    pois através de uma regressão linear realizada na etapa de análise foi visto que é possível colocar para score 1 uma idade mínima de 20 e para score 10, 90.

    Attributes
    ----------
    dataset : pd.DataFrame
        Dataset a ser modificado

    Methods
    -------
    execute()
        Executa a criação da coluna scaled_hle para normalização.
    
    """

    __name__ = 'ScaledHle'

    def __init__(self, dataset: pd.DataFrame):    
        self.dataset = dataset

    def execute(self):        
        self.dataset['scaled_hle'] = [self.min_max_scaler(x) for x in self.dataset['hle']]
        return self.dataset

    def min_max_scaler(self, x):
        min = 20
        max = 90
        X_std = (x - min) / (max - min)
        X_scaled = X_std * 1
        return X_scaled