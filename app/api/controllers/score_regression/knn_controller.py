from fastapi import APIRouter
from app.entities.request.country_data import CountryData
from app.entities.response.prediction_result import PredictionResult
from app.entities.response.regression_model_evaluation_response import RegressionModelEvaluationResponse
from models.classification.knn_classifier_model import KnnClassifierModel
from services.model_service import ModelService
from services.regression_model_evaluation_service import RegressionModelEvaluationService
from models.regression.knn_model import KnnModel

router = APIRouter(prefix="/score-regression/knn", tags=["KNeighborsRegressor"])

@router.get("/evaluate", response_model=list[RegressionModelEvaluationResponse])
def evaluate_model() -> list[RegressionModelEvaluationResponse]:
    evaluation_service = RegressionModelEvaluationService(KnnModel())
    evaluation = evaluation_service.evaluate()
    return evaluation

@router.put('/predict', response_model=PredictionResult)
def predict(data: CountryData) -> PredictionResult:
    prediction_result = ModelService(KnnModel(), KnnClassifierModel()).get_prediction_results(data)
    return prediction_result