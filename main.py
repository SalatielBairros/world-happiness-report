from fastapi import FastAPI
from environment.env_configuration import prepare_environment
from app.api.controllers.index_controller import router as index_router
from app.api.controllers.score_regression.rf_controller import router as rf_router
from app.api.controllers.score_regression.knn_controller import router as knn_router
from app.api.controllers.ingestion.data_ingestion_controller import router as data_ingestion_router
from app.api.controllers.region_classification.rf_region_controller import router as rf_region_router
from app.api.controllers.region_classification.knn_region_controller import router as knn_region_router
from fastapi.openapi.utils import get_openapi

prepare_environment()
app = FastAPI()
app.include_router(index_router)
app.include_router(rf_router)
app.include_router(knn_router)
app.include_router(data_ingestion_router)
app.include_router(rf_region_router)
app.include_router(knn_region_router)

app.openapi_schema = get_openapi(
    title="World Happiness Report ML Models",
    version="1.0",
    description="API with ML Models for World Happiness Report.",
    routes=app.routes,
    contact={
        "name": "Salatiel Bairros",
        "email": "salatiel.costabairros@gmail.com"
    }
)