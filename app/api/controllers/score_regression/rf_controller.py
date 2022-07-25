from fastapi import APIRouter
from app.entities.request.country_data import CountryData
from app.entities.response.prediction_result import PredictionResult
from app.entities.response.regression_model_evaluation_response import RegressionModelEvaluationResponse
from models.classification.random_forest_classifier_model import RandomForestClassifierModel
from services.model_service import ModelService
from services.regression_model_evaluation_service import RegressionModelEvaluationService
from models.regression.random_forest_model import RandomForestRegressorModel

router = APIRouter(prefix="/score-regression/random-forest", tags=["RandomForestRegressor"])

@router.get("/evaluate", response_model=list[RegressionModelEvaluationResponse])
def evaluate_model() -> list[RegressionModelEvaluationResponse]:
    evaluation_service = RegressionModelEvaluationService(RandomForestRegressorModel())
    evaluation = evaluation_service.evaluate()
    return evaluation

@router.put('/predict', response_model=PredictionResult)
def predict(data: CountryData) -> PredictionResult:
    prediction_result = ModelService(RandomForestRegressorModel(), RandomForestClassifierModel()).get_prediction_results(data)
    return prediction_result