from pydantic import BaseModel

class ClassificationModelEvaluationResponse(BaseModel):
    accuracy: float
    precision: float
    recall: float
    f1_score: float    
    confusion_matrix: list[list[int]]
    roc_auc_score: float
    report_by_label: dict
    feature_importances: list