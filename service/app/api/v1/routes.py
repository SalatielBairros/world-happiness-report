from fastapi import APIRouter

from app.api.v1.endpoints import fetch_dataset

api_router_v1 = APIRouter()

api_router_v1.include_router(fetch_dataset.router_v1)
