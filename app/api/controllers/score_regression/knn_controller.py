from fastapi import APIRouter
from services.model_evaluation_service import ModelEvaluationService
from models.regression.knn_model import KnnModel

router = APIRouter(prefix="/knn")

@router.get("/evaluate")
def evaluate_model():
    evaluation_service = ModelEvaluationService(KnnModel())
    evaluation = evaluation_service.evaluate()
    return evaluation
