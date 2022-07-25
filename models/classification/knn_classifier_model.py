from models.base_learning_model import BaseLearningModel
from sklearn.neighbors import KNeighborsClassifier

class KnnClassifierModel(BaseLearningModel):
    def __init__(self, target_column: str = 'cat_region'):
        super().__init__(target_column)

    def get_model(self):
        return KNeighborsClassifier()

    def get_model_name(self) -> str:
        return 'knn_region_classifier'