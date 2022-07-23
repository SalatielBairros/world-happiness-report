from fastapi import FastAPI
from environment.env_configuration import prepare_environment 
from app.api.controllers.index_controller import router as index_router

prepare_environment()
app = FastAPI()
app.include_router(index_router)