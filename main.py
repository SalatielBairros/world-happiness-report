from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.config.tags_metadata import tags_metadata

from app.api.v1.routes import api_router_v1

app = FastAPI (
  title="WHR TCC at PUC-Minas",
  description="Some description",
  version="1.0.0",
  openapi_tagas=tags_metadata
)

app.add_middleware (
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(api_router_v1, prefix="/v1")
