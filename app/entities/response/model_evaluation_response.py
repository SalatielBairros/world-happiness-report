from pydantic import BaseModel

class ModelEvaluationResponse(BaseModel):
    year: int
    r2: float
    adjusted_r2: float
    mean_squared_error: float
    sqrt_mean_squared_error: float