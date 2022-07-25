from fastapi import APIRouter
from app.entities.response.regression_model_evaluation_response import RegressionModelEvaluationResponse
from services.regression_model_evaluation_service import RegressionModelEvaluationService
from models.regression.random_forest_model import RandomForestRegressorModel

router = APIRouter(prefix="/score-regression/random-forest", tags=["RandomForestRegressor"])

@router.get("/evaluate", response_model=list[RegressionModelEvaluationResponse])
def evaluate_model() -> list[RegressionModelEvaluationResponse]:
    evaluation_service = RegressionModelEvaluationService(RandomForestRegressorModel())
    evaluation = evaluation_service.evaluate()
    return evaluation
