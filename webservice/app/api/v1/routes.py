from fastapi import APIRouter

from app.api.v1.endpoints import hello_world

api_router_v1 = APIRouter()

api_router_v1.include_router(hello_world.router_v1)
