from fastapi import APIRouter
from data_ingestion.whr_data_ingestion import WhrDataIngestion
import json

router = APIRouter(prefix="/data-ingestion", tags=["Data ingestion"])

@router.post("/ingest")
def evaluate_model():
    ingestor = WhrDataIngestion()
    ingested_data = ingestor.ingest()