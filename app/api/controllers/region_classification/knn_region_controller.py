from fastapi import APIRouter, Response, status
from app.entities.request.country_data import CountryData
from app.entities.response.classification_model_evaluation_data import ClassificationModelEvaluationData
from app.entities.response.classification_model_evaluation_response import ClassificationModelEvaluationResponse
from app.entities.response.prediction_result import PredictionResult
from services.classification_model_evaluation_service import ClassificationModelEvaluationService
from models.classification.knn_classifier_model import KnnClassifierModel
from models.regression.knn_model import KnnModel
from services.model_service import ModelService

router = APIRouter(prefix="/region-classification/knn", tags=["KnnClassifier"])

@router.get("/evaluate", response_model=ClassificationModelEvaluationData)
def evaluate_model(response: Response):
    try:
        evaluation_service = ClassificationModelEvaluationService(KnnClassifierModel())
        evaluation = evaluation_service.evaluate()
        return evaluation
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Evaluate failed", "error": str(e)}

@router.get("/balanced/evaluate", response_model=ClassificationModelEvaluationResponse)
def evaluate_model(response: Response):
    try:
        evaluation_service = ClassificationModelEvaluationService(KnnClassifierModel())
        evaluation = evaluation_service.evaluate_augmentaded_data()
        return evaluation
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Balance evaluate failed", "error": str(e)}

@router.put('/predict', response_model=PredictionResult)
def predict(data: CountryData, response: Response) -> PredictionResult:
    try:
        prediction_result = ModelService(KnnModel(), KnnClassifierModel()).get_prediction_results(data)
        return prediction_result
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Predict failed", "error": str(e)}
