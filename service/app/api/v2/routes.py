from fastapi import APIRouter

from app.api.v2.endpoints import hello_world

api_router_v2 = APIRouter()

api_router_v2.include_router(hello_world.router_v2)
