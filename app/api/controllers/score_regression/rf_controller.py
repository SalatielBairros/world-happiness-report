from fastapi import APIRouter
from services.regression_model_evaluation_service import RegressionModelEvaluationService
from models.regression.random_forest_model import RandomForestModel

router = APIRouter(prefix="/random-forest", tags=["RandomForestRegressor"])

@router.get("/evaluate")
def evaluate_model():
    evaluation_service = RegressionModelEvaluationService(RandomForestModel())
    evaluation = evaluation_service.evaluate()
    return evaluation
