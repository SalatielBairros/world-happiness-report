from fastapi import APIRouter

router_v1 = APIRouter()

@router_v1.get(
  "/hello-world",
  status_code=200,
  tags=["Hello world"]
)
def read_root():
  return { "Hello": "World V1" }

@router_v1.get(
  "/hello-world-2",
  status_code=200,
  tags=["Hello world"]
)
def read_root_2():
  return { "Hello": "World V1-2" }
