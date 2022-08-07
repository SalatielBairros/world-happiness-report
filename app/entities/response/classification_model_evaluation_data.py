from typing import List
from pydantic import BaseModel

class ClassificationModelEvaluationData(BaseModel):
    accuracy: float
    precision: float
    recall: float
    f1_score: float    
    confusion_matrix: List[List[int]]
    report_by_label: dict
    feature_importances: list
