import pandas as pd
from repository.local_storage_repository import LocalStorageRepository
from data_augmentation.commands_handler import Commands
from data_augmentation.balancing_train_data import BalancingTrainData
from data_augmentation.separating_validation_data import SeparatingValidationData
from data_augmentation.balancing_all_dataset import BalancingAllDataset
import logging

def execute_data_augmentation() -> pd.DataFrame:
    logging.info('Loading prepared data from local storage')
    repository = LocalStorageRepository()
    balanced_dataset = repository.get_augmented_dataset()

    if(balanced_dataset is None):        
        return Commands(repository) \
            .add_command(BalancingAllDataset) \
            .add_command(SeparatingValidationData) \
            .add_command(BalancingTrainData) \
            .execute_and_save()

    return balanced_dataset