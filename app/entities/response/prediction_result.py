from pydantic import BaseModel

class PredictionResult(BaseModel):
    original_score: float
    original_region: int
    predicted_score: float
    predicted_region: int
    predicted_score_with_predicted_region: float
    predicted_region_with_predicted_score: int