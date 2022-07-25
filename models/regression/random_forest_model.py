from models.base_learning_model import BaseLearningModel
from sklearn.ensemble import RandomForestRegressor
from environment.constants import EnvironmentVariables

class RandomForestRegressorModel(BaseLearningModel):
    def get_model(self):
        return RandomForestRegressor(random_state=EnvironmentVariables.SEED, max_depth = 10)