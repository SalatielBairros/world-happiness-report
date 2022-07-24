from app.entities.response.classification_model_evaluation_response import ClassificationModelEvaluationResponse
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
        self.columns = []

    def evaluate(self, train_data: pd.DataFrame) -> ClassificationModelEvaluationResponse:        
        logging.info("Evaluating model...")
        X = train_data.drop(columns=self.model.target_column)
        y = train_data[self.model.target_column]
        self.columns = X.columns
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=EnvironmentVariables.SEED, stratify=y)
        
        model = self.model.get_model()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        y_pred_proba = model.predict_proba(x_test)[::, 1]
       
        return self.__get_metrics__(y_test, y_pred, y_pred_proba)

    def evaluate_augmentaded_data(self, balanced_dataset: pd.DataFrame = None) -> dict:
        if(balanced_dataset is None):
            balanced_dataset = self.repository.load_balanced_dataset()

        x_balanced = balanced_dataset.drop(columns=['isFraud']).values
        y_balanced = balanced_dataset['isFraud'].values
        self.columns = balanced_dataset.drop(columns=['isFraud']).columns
        x_train, x_test, y_train, y_test = train_test_split(x_balanced, y_balanced, test_size=0.15, random_state = EnvironmentVariables.SEED, stratify=y_balanced)
        
        test_model = self.model.get_model()
        test_model.fit(x_train, y_train)
        y_test_pred = test_model.predict(x_test)
        y_test_pred_proba = test_model.predict_proba(x_test)[::, 1]

        validation_dataset = self.repository.load_validation_dataset()
        validation_model = self.model.get_model()
        validation_model.fit(x_balanced, y_balanced)
        x_validation = validation_dataset.drop(columns=['isFraud']).values
        y_validation = validation_dataset['isFraud'].values
        y_validation_pred = validation_model.predict(x_validation)
        y_validation_pred_proba = validation_model.predict_proba(x_validation)[::, 1]

        test_metrics = self.__get_metrics__(y_test, y_test_pred, y_test_pred_proba, x_test, test_model)
        validation_metrics = self.__get_metrics__(y_validation, y_validation_pred, y_validation_pred_proba, x_validation, validation_model)

        return {
            'test_metrics': test_metrics.dict(),
            'validation_metrics': validation_metrics.dict()
        }

    def __get_metrics__(self, y_real, y_pred, y_pred_proba, x_test, model) -> ClassificationModelEvaluationResponse:
        accuracy = metrics.accuracy_score(y_real, y_pred)
        precision = metrics.precision_score(y_real, y_pred)
        recall = metrics.recall_score(y_real, y_pred)
        f1 = metrics.f1_score(y_real, y_pred)
        cm = confusion_matrix(y_real, y_pred).tolist()
        auc = metrics.roc_auc_score(y_real, y_pred_proba)

        report = metrics.classification_report(y_real, y_pred, output_dict=True,target_names=['NotFraud', 'Fraud'])
        report = {
            'Fraud': report['Fraud'],
            'NotFraud': report['NotFraud']
        }

        perm = PermutationImportance(model, random_state=EnvironmentVariables.SEED).fit(x_test, y_real)
        importances = list(zip(self.columns, np.round(perm.feature_importances_, 2)))
        
        return ClassificationModelEvaluationResponse(
            accuracy=accuracy, 
            precision=precision, 
            recall=recall, 
            f1_score=f1,
            confusion_matrix=cm,
            roc_auc_score=auc,
            report_by_label=report,
            feature_importances=importances)