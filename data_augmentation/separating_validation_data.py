import pandas as pd
from sklearn.model_selection import train_test_split
from environment.constants import EnvironmentVariables
from repository.local_storage_repository import LocalStorageRepository

class SeparatingValidationData:
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset
        self.repository = LocalStorageRepository()

    def execute(self) -> pd.DataFrame:        
        X = self.dataset.drop('cat_region', axis=1)
        y = self.dataset['cat_region']
        x_model, x_validation, y_model, y_validation = train_test_split(X, y, test_size=0.15, random_state = EnvironmentVariables.SEED, stratify=y)
        
        x_validation['cat_region'] = y_validation
        self.repository.save_validation_dataset(x_validation)

        x_model['cat_region'] = y_model       
        return x_model
        