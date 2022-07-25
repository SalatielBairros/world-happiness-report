from app.entities.response.classification_model_evaluation_response import ClassificationModelEvaluationResponse
from app.entities.response.classification_model_evaluation_data import ClassificationModelEvaluationData
import logging
from sklearn.model_selection import train_test_split
from models.base_learning_model import BaseLearningModel
from environment.constants import EnvironmentVariables
import pandas as pd
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from repository.local_storage_repository import LocalStorageRepository
from eli5.sklearn import PermutationImportance
import numpy as np

class ClassificationModelEvaluationService:
    def __init__(self, model: BaseLearningModel) -> None:
        self.model = model
        self.repository = LocalStorageRepository()
        self.drop_from_processed_dataset = ['country', 'region', 'hle', 'year', 'cat_country', 'rounded_score']
        self.columns = []

    def evaluate(self, train_data: pd.DataFrame = None) -> ClassificationModelEvaluationData:
        if(train_data is None):
            train_data = self.repository.get_processed_dataset().drop(columns=self.drop_from_processed_dataset)

        logging.info("Evaluating model...")
        X = train_data.drop(columns=self.model.target_column)
        y = train_data[self.model.target_column]
        self.columns = X.columns
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=EnvironmentVariables.SEED, stratify=y)
        
        model = self.model.get_model()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
       
        return self.__get_metrics__(y_test, y_pred, x_test, model)

    def evaluate_augmentaded_data(self, balanced_dataset: pd.DataFrame = None) -> ClassificationModelEvaluationResponse:
        if(balanced_dataset is None):
            balanced_dataset = self.repository.get_augmented_dataset()
        
        x_balanced = balanced_dataset.drop(columns=[self.model.target_column]).values
        y_balanced = balanced_dataset[self.model.target_column].values
        self.columns = balanced_dataset.drop(columns=[self.model.target_column]).columns
        x_train, x_test, y_train, y_test = train_test_split(x_balanced, y_balanced, test_size=0.2, random_state = EnvironmentVariables.SEED, stratify=y_balanced)
        
        test_model = self.model.get_model()
        test_model.fit(x_train, y_train)
        y_test_pred = test_model.predict(x_test)

        validation_dataset = self.repository.get_validation_dataset()
        validation_model = self.model.get_model()
        validation_model.fit(x_balanced, y_balanced)
        x_validation = validation_dataset.drop(columns=[self.model.target_column]).values
        y_validation = validation_dataset[self.model.target_column].values
        y_validation_pred = validation_model.predict(x_validation)

        test_metrics = self.__get_metrics__(y_test, y_test_pred, x_test, test_model)
        validation_metrics = self.__get_metrics__(y_validation, y_validation_pred, x_validation, validation_model)

        return ClassificationModelEvaluationResponse(
            test_data_evaluation=test_metrics,
            validation_data_evaluation=validation_metrics)

    def __get_metrics__(self, y_real, y_pred, x_test, model) -> ClassificationModelEvaluationData:
        accuracy = metrics.accuracy_score(y_real, y_pred)
        precision = metrics.precision_score(y_real, y_pred, average='weighted')
        recall = metrics.recall_score(y_real, y_pred, average='weighted')
        f1 = metrics.f1_score(y_real, y_pred, average='weighted')
        cm = confusion_matrix(y_real, y_pred).tolist()

        report = metrics.classification_report(y_real, y_pred, output_dict=True,target_names=self.__get_regions__())
        perm = PermutationImportance(model, random_state=EnvironmentVariables.SEED).fit(x_test, y_real)
        importances = list(zip(self.columns, np.round(perm.feature_importances_, 2)))
        
        return ClassificationModelEvaluationData(
            accuracy=accuracy, 
            precision=precision, 
            recall=recall, 
            f1_score=f1,
            confusion_matrix=cm,
            report_by_label=report,
            feature_importances=importances)

    def __get_regions__(self) -> list:
        processed_dataset = self.repository.get_processed_dataset()
        region_names = processed_dataset.groupby('cat_region')['region'].first().to_dict()
        return list(region_names.values())
