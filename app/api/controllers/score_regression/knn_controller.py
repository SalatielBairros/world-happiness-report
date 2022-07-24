from fastapi import APIRouter
from services.regression_model_evaluation_service import RegressionModelEvaluationService
from models.regression.knn_model import KnnModel

router = APIRouter(prefix="/knn", tags=["KNeighborsRegressor"])

@router.get("/evaluate")
def evaluate_model():
    evaluation_service = RegressionModelEvaluationService(KnnModel())
    evaluation = evaluation_service.evaluate()
    return evaluation
