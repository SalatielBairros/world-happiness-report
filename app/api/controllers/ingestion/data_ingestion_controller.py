from fastapi import APIRouter
from data_ingestion.whr_data_ingestion import WhrDataIngestion
import json

router = APIRouter(prefix="/data-ingestion", tags=["Data ingestion"])

@router.get("/ingest")
def evaluate_model():
    ingestor = WhrDataIngestion()
    ingested_data = ingestor.ingest()
    return json.loads(ingested_data.to_dict(orient="records"))
