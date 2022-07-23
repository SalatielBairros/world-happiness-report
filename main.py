from fastapi import FastAPI
from environment.env_configuration import prepare_environment 
from app.api.controllers.index_controller import router as index_router
from app.api.controllers.score_regression.rf_controller import router as rf_router
from app.api.controllers.score_regression.knn_controller import router as knn_router
from app.api.controllers.ingestion.data_ingestion_controller import router as data_ingestion_router

prepare_environment()
app = FastAPI()
app.include_router(index_router)
app.include_router(rf_router)
app.include_router(knn_router)
app.include_router(data_ingestion_router)