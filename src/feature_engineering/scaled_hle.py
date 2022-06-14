import pandas as pd

class ScaledHle():
    """
    Com o propósito de melhorar a visualização dos dados, cria uma escala de HLE entre 0 e 1 utilizando o MinMaxScaler.
    No entanto é utilizado um intervalo customizado, 
    pois através de uma regressão linear realizada na etapa de análise foi visto que é possível colocar para score 1 uma idade mínima de 20 e para score 10, 90.

    Attributes
    ----------
    output_directory : str
        Diretório base onde os datasets são armazenados e os modificados serão salvos.
    input_file : str
        Arquivo do dataset de origem

    Methods
    -------
    execute()
        Executa a criação da coluna scaled_hle para normalização.
    
    """

    __name__ = 'ScaledHle'

    def __init__(self, output_directory = './data/feature_engineering', input_file='./data/feature_engineering/rounded_score.csv'):    
        self.output_directory = output_directory
        self.input_file = input_file

    def execute(self):
        dataset = pd.read_csv(self.input_file)
        dataset['scaled_hle'] = [self.min_max_scaler(20, 90, x) for x in dataset['hle']]
        dataset.to_csv(self.output_directory + '/scaled_hle.csv', index=False)

    def min_max_scaler(self, min, max, x):
        X_std = (x - min) / (max - min)
        X_scaled = X_std * 1
        return X_scaled