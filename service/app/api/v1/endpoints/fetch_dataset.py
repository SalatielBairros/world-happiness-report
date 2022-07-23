from fastapi import APIRouter

from app.api.helpers.fetch_dataset import FetchDataset

router_v1 = APIRouter()

@router_v1.get(
  "/fetch-dataset",
  status_code=200,
  tags=["BUSCAR DATASET COMPLETO"]
)
def fetch_complete_dataset():
  return FetchDataset().fetched_dataset()

