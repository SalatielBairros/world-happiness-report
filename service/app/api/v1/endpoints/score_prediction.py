from fastapi import APIRouter

from app.api.helpers.score_prediction import ScorePrediction

router_v1 = APIRouter()

@router_v1.get(
  "/score-prediction",
  status_code=200,
  tags=["PREDIÇÃO DO SCORE"]
)
def score_prediction():
  return ScorePrediction().construct_model()

