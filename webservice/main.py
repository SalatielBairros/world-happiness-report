from sys import prefix
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.routes import api_router_v1
from app.api.v2.routes import api_router_v2

app = FastAPI (
  title="World Happiness Report"
)

app.add_middleware (
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(api_router_v1, prefix="/v1")
app.include_router(api_router_v2, prefix="/v2")
