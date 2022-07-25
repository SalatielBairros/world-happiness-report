from fastapi import APIRouter
from services.classification_model_evaluation_service import ClassificationModelEvaluationService
from models.classification.random_forest_classifier_model import RandomForestClassifierModel
from app.entities.response.classification_model_evaluation_data import ClassificationModelEvaluationData
from app.entities.response.classification_model_evaluation_response import ClassificationModelEvaluationResponse

router = APIRouter(prefix="/region-classification/random-forest", tags=["RandomForestClassifier"])

@router.get("/evaluate", response_model=ClassificationModelEvaluationData)
def evaluate_model():
    evaluation_service = ClassificationModelEvaluationService(RandomForestClassifierModel())
    evaluation = evaluation_service.evaluate()
    return evaluation

@router.get("/balanced/evaluate", response_model=ClassificationModelEvaluationResponse)
def evaluate_model():
    evaluation_service = ClassificationModelEvaluationService(RandomForestClassifierModel())
    evaluation = evaluation_service.evaluate_augmentaded_data()
    return evaluation
