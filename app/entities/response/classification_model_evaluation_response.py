from pydantic import BaseModel
from app.entities.response.classification_model_evaluation_data import ClassificationModelEvaluationData

class ClassificationModelEvaluationResponse(BaseModel):
    test_data_evaluation: ClassificationModelEvaluationData
    validation_data_evaluation: ClassificationModelEvaluationData