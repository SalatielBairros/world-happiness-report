from fastapi import APIRouter
from data_ingestion.whr_data_ingestion import WhrDataIngestion
from repository.local_storage_repository import LocalStorageRepository

router = APIRouter(prefix="/data-ingestion", tags=["Data ingestion"])

@router.post("/ingest")
def evaluate_model():
    ingestor = WhrDataIngestion()
    ingestor.ingest()

@router.get("/ingested/processed-data")
def get_processed_data():
    repository = LocalStorageRepository()
    return repository.get_processed_dataset().to_dict(orient='records')

@router.get("/ingested/pandemic-data")
def get_pandemic_data():
    repository = LocalStorageRepository()
    return repository.get_pandemic_dataset().to_dict(orient='records')