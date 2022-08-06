from models.base_learning_model import BaseLearningModel
from sklearn.ensemble import RandomForestClassifier
from environment.constants import EnvironmentVariables

class RandomForestClassifierModel(BaseLearningModel):
    def __init__(self, target_column: str = 'cat_region', uses_balanced_dataset: bool = True):
        super().__init__(target_column, uses_balanced_dataset)

    def get_model(self):
        return RandomForestClassifier(random_state=EnvironmentVariables.SEED)

    def get_model_name(self) -> str:
        return 'random_forest_region_classifier'