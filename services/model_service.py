import pandas as pd
from app.entities.response.prediction_result import PredictionResult
from environment.constants import DatasetConstants
from models.base_learning_model import BaseLearningModel
from app.entities.request.country_data import CountryData
from repository.local_storage_repository import LocalStorageRepository
from feature_engineering.scaled_hle import ScaledHle
from lib.io_helper import create_directory_if_not_exists
import joblib

class ModelService:
    def __init__(self, regression_model: BaseLearningModel, classification_model: BaseLearningModel):
        self.columns_to_drop_x = DatasetConstants.COLUMNS_TO_DROP_TO_TRAINING
        self.regression_model = regression_model
        self.classification_model = classification_model
        self.repository = LocalStorageRepository()

        if(self.regression_model is None or self.classification_model is None):
            raise Exception('ModelService: __init__: regression_model or classification_model is None')

        create_directory_if_not_exists('./data/models')        

    def get_prediction_results(self, data: CountryData) -> PredictionResult:        
        regression = self.__load_regression_model__()
        classification = self.__load_classification_model__()        
        df_data = pd.DataFrame(data.dict(), index=[0])
        df_data['scaled_hle'] = ScaledHle(None).min_max_scaler(data.hle)
        df_data.drop(columns=['hle'], inplace=True)

        score_prediction = regression.predict(df_data.drop(columns=[self.regression_model.target_column]))
        region_prediction = classification.predict(df_data.drop(columns=[self.classification_model.target_column]))

        df_data[self.regression_model.target_column] = score_prediction
        df_data[self.classification_model.target_column] = region_prediction

        score_with_predicted_region = regression.predict(df_data.drop(columns=[self.regression_model.target_column]))
        region_with_predicted_score = classification.predict(df_data.drop(columns=[self.classification_model.target_column]))

        return PredictionResult(
            original_score=data.score,
            original_region=data.cat_region,
            predicted_score=score_prediction,
            predicted_region=region_prediction,
            predicted_score_with_predicted_region=score_with_predicted_region,
            predicted_region_with_predicted_score=region_with_predicted_score
        )

    def __load_regression_model__(self):
        return self.__load_model__(self.regression_model)

    def __load_classification_model__(self):
        return self.__load_model__(self.classification_model)

    def __load_model__(self, model_implementation: BaseLearningModel):
        model = model_implementation.load_model()
        if(model is None):
            model = model_implementation.get_model()
            X, y  = self.__get_data__(model_implementation.target_column, model_implementation.uses_balanced_dataset)
            model.fit(X, y)
            model_name = model_implementation.get_model_name()
            joblib.dump(model, f'./data/models/{model_name}.joblib')
        return model

    def __get_data__(self, target_column: str, balanced: bool):
        dataset = None
        if(balanced):
            dataset = self.repository.get_full_augmented_dataset()
        else:
            dataset = self.repository.get_processed_dataset().drop(columns=self.columns_to_drop_x)

        X = dataset.drop(columns=[target_column])
        y = dataset[target_column]

        return X, y
    