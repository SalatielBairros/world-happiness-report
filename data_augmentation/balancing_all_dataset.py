import pandas as pd
from imblearn.over_sampling import SMOTE
from repository.local_storage_repository import LocalStorageRepository
from environment.constants import EnvironmentVariables, DatasetConstants

class BalancingAllDataset:
    def __init__(self, to_balance_dataset: pd.DataFrame) -> None:
        self.to_balance_dataset = to_balance_dataset
        self.repository = LocalStorageRepository()

    def execute(self):
        self.to_balance_dataset.drop(columns=DatasetConstants.COLUMNS_TO_DROP_TO_TRAINING, inplace=True)
        X = self.to_balance_dataset.drop('cat_region', axis=1)
        y = self.to_balance_dataset['cat_region']
        smote = SMOTE(sampling_strategy='not majority', random_state=EnvironmentVariables.SEED)
        x_resampled, y_resampled = smote.fit_resample(X, y)
        df_balanced = pd.concat([y_resampled, x_resampled], axis=1)
        self.repository.save_full_augmented_dataset(df_balanced)
        return self.to_balance_dataset