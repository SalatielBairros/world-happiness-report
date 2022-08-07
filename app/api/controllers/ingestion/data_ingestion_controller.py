from fastapi import APIRouter, Response, status
from data_ingestion.whr_data_ingestion import WhrDataIngestion
from repository.local_storage_repository import LocalStorageRepository

router = APIRouter(prefix="/data-ingestion", tags=["Data ingestion"])
_repository = LocalStorageRepository()

@router.post("/ingest")
def evaluate_model(response: Response):
    try:
        ingestor = WhrDataIngestion()
        ingestor.ingest()
        response.status_code = status.HTTP_201_CREATED
        return {"message": "Data ingestion completed successfully"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Data ingestion failed", "error": str(e)}

@router.get("/ingested/processed-data")
def get_processed_data(response: Response):
    try:
        return _repository.get_processed_dataset().to_dict(orient='records')
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Error to get processed data", "error": str(e)}

@router.get("/ingested/pandemic-data")
def get_pandemic_data(response: Response):
    try:
        repository = LocalStorageRepository()
        return repository.get_pandemic_dataset().to_dict(orient='records')
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Pandemic data ingestion failed", "error": str(e)}
