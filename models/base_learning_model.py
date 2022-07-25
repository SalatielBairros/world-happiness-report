
from abc import ABCMeta, abstractmethod
import joblib
from os import path

class BaseLearningModel(metaclass=ABCMeta):
    def __init__(self, target_column: str = 'score'):
        self.target_column = target_column
        self.model = None

    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        pass

    def load_model(self) -> None:
        model_path = f'./data/models/{self.get_model_name()}.joblib'
        if(path.exists(model_path)):
            return joblib.load(model_path)
        return None