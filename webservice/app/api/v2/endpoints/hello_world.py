from fastapi import APIRouter

router_v2 = APIRouter()

@router_v2.get("/hello-world")
def read_root():
  return { "Hello": "World V2" }
