from fastapi import APIRouter
from app.entities.response.regression_model_evaluation_response import RegressionModelEvaluationResponse
from services.regression_model_evaluation_service import RegressionModelEvaluationService
from models.regression.knn_model import KnnModel

router = APIRouter(prefix="/score-regression/knn", tags=["KNeighborsRegressor"])

@router.get("/evaluate", response_model=list[RegressionModelEvaluationResponse])
def evaluate_model() -> list[RegressionModelEvaluationResponse]:
    evaluation_service = RegressionModelEvaluationService(KnnModel())
    evaluation = evaluation_service.evaluate()
    return evaluation
