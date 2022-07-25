from fastapi import APIRouter
from app.entities.response.classification_model_evaluation_data import ClassificationModelEvaluationData
from app.entities.response.classification_model_evaluation_response import ClassificationModelEvaluationResponse
from services.classification_model_evaluation_service import ClassificationModelEvaluationService
from models.classification.knn_classifier_model import KnnClassifierModel

router = APIRouter(prefix="/region-classification/knn", tags=["KnnClassifier"])

@router.get("/evaluate", response_model=ClassificationModelEvaluationData)
def evaluate_model():
    evaluation_service = ClassificationModelEvaluationService(KnnClassifierModel())
    evaluation = evaluation_service.evaluate()
    return evaluation

@router.get("/balanced/evaluate", response_model=ClassificationModelEvaluationResponse)
def evaluate_model():
    evaluation_service = ClassificationModelEvaluationService(KnnClassifierModel())
    evaluation = evaluation_service.evaluate_augmentaded_data()
    return evaluation
