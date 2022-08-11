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
def get_processed_data(columns:str, response: Response):
    try:        
        processed_dataset = _repository.get_processed_dataset()
        columns_list = __get_columns__(columns)
        if(columns_list is not None):
            processed_dataset = processed_dataset[columns_list]
        return processed_dataset.to_dict(orient='records')
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Error to get processed data", "error": str(e)}

@router.get("/ingested/pandemic-data")
def get_pandemic_data(response: Response):
    try:
        return _repository.get_pandemic_dataset().to_dict(orient='records')
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Pandemic data ingestion failed", "error": str(e)}

@router.get("/ingested/processed-data/grouped")
def get_grouped_data(group_by:str, columns:str, response: Response, country:str=None, region:str=None):
    try:
        processed_dataset = _repository.get_processed_dataset()
        if(region is not None):
            processed_dataset = processed_dataset[processed_dataset["region"] == region]
        if(country is not None):
            processed_dataset = processed_dataset[processed_dataset["country"] == country]

        grouped_data = processed_dataset.groupby(by=group_by).mean().reset_index().sort_values(by=group_by, ascending=True)
        columns_list = __get_columns__(columns)
        if(columns_list is not None):
            grouped_data = grouped_data[columns_list]
        return grouped_data.to_dict(orient='records')
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Error to get grouped data", "error": str(e)}

@router.get("/ingested/processed-data/countries")
def get_countries(response: Response):
    try:
        countries = _repository.get_processed_dataset()['country'].unique().tolist()
        return {
            'data': countries
        }
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Error to get countries", "error": str(e)}

@router.get("/ingested/processed-data/regions")
def get_regions(response: Response):
    try:
        regions = _repository.get_processed_dataset()['region'].unique().tolist()
        return {
            'data': regions
        }
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Error to get regions", "error": str(e)}

@router.get("/ingested/processed-data/correlations")
def get_correlations(columns:str, response: Response):
    try:
        processed_dataset = _repository.get_processed_dataset()
        columns_list = __get_columns__(columns)
        if(columns_list is not None):
            processed_dataset = processed_dataset[columns_list]
        correlations = processed_dataset.corr()
        return correlations.to_dict(orient='list')
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Error to get correlations", "error": str(e)}

@router.get("/ingested/processed-data/pandemic/grouped")
def get_pandemic_grouped_data(group_by:str, columns:str, response: Response, country:str=None, region:str=None):
    try:
        processed_dataset = _repository.get_pandemic_dataset()
        if(region is not None):
            processed_dataset = processed_dataset[processed_dataset["region"] == region]
        if(country is not None):
            processed_dataset = processed_dataset[processed_dataset["country"] == country]

        grouped_data = processed_dataset.groupby(by=group_by).mean().reset_index().sort_values(by=group_by, ascending=True)
        columns_list = __get_columns__(columns)
        if(columns_list is not None):
            grouped_data = grouped_data[columns_list]
        return grouped_data.to_dict(orient='records')
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Error to get pandemic grouped data", "error": str(e)}

def __get_columns__(columns:str) -> list[str]:
    if(columns is not None and len(columns.strip()) > 0):
        return columns.split(",")
    return None