from pydantic import BaseModel

class ClassificationModelEvaluationData(BaseModel):
    accuracy: float
    precision: float
    recall: float
    f1_score: float    
    confusion_matrix: list[list[int]]
    report_by_label: dict
    feature_importances: list
