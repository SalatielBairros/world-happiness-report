from fastapi import APIRouter

from modeling.data_preparation_commands import DataPreparation

router_v1 = APIRouter()

@router_v1.get("/hello-world")
def read_root():
  return { "Hello": "World V1" }

@router_v1.get("/hello-world-2")
def read_root_2():
  return { "Hello": "World V1-2" }

@router_v1.get("/data-preparation")
def data_preparation():
  return DataPreparation()
