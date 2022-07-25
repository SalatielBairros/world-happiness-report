
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

    def save_model(self) -> None:
        if(self.model is not None):
            model_name = self.get_model_name()
            joblib.dump(self.model, f'./data/models/{model_name}.joblib')
        else:
            raise Exception('Model not initialized')

    def load_model(self) -> None:
        model_path = f'./data/models/{self.get_model_name()}.joblib'
        if(path.exists(model_path)):
            self.model = joblib.load(model_path)
        else:
            self.model = self.get_model()