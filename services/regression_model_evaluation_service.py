import pandas as pd
from app.entities.response.regression_model_evaluation_response import RegressionModelEvaluationResponse
from sklearn import metrics
import numpy as np
from environment.constants import EnvironmentVariables
from models.base_learning_model import BaseLearningModel
from repository.local_storage_repository import LocalStorageRepository
from eli5.sklearn import PermutationImportance

class RegressionModelEvaluationService:
    def __init__(self, model: BaseLearningModel) -> None:
        self.columns_to_drop_x = ['country', 'region', 'score', 'year', 'cat_country', 'rounded_score', 'scaled_hle']
        self.model = model
        self.repository = LocalStorageRepository()

    def evaluate(self) -> list[RegressionModelEvaluationResponse]:
        dataset = self.repository.get_processed_dataset()
        if(dataset is None):
            raise Exception('Dataset is empty')

        return self.__year_cross_validation__(dataset)        

    def __get_metrics__(self, y_real, y_pred, x_test, model, year) -> RegressionModelEvaluationResponse:
        r2 = metrics.r2_score(y_real, y_pred)
        n = len(y_real)
        p = len(x_test.columns)
        r2_adj = 1-(1-r2)*(n-1)/(n-p-1)
        mean_squared_error = metrics.mean_squared_error(y_real, y_pred)
        sqrt_mse = np.sqrt(mean_squared_error)

        perm = PermutationImportance(model, random_state=EnvironmentVariables.SEED).fit(x_test, y_real)
        importances = list(zip(x_test.columns, np.round(perm.feature_importances_, 2)))
        
        return RegressionModelEvaluationResponse(
            year=year,
            r2=r2,
            adjusted_r2=r2_adj,
            mean_squared_error=mean_squared_error,
            sqrt_mean_squared_error=sqrt_mse,
            importances=importances
        )

    def __year_cross_validation__(self, dataset: pd.DataFrame):
        current_year = dataset['year'].min()
        last_year = dataset['year'].max()
        years = list(range(current_year, last_year+1))
        results = []
        for year in years:
            to_train = dataset.query(f'year != {year}')
            to_test = dataset.query(f'year == {year}')
            X = to_train.drop(self.columns_to_drop_x, axis=1)
            y = to_train[self.model.target_column]
            X_test = to_test.drop(self.columns_to_drop_x, axis=1)
            y_test = to_test[self.model.target_column]

            model = self.model.get_model()
            model.fit(X, y)        
            result = self.__get_metrics__(y_test, model.predict(X_test), X_test, model, year)
        
            results.append(result)

        return results