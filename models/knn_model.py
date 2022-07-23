from models.base_learning_model import BaseLearningModel
from sklearn.neighbors import KNeighborsRegressor

class KnnModel(BaseLearningModel):
    def get_model(self):
        return KNeighborsRegressor(n_neighbors=5)