from fastapi import APIRouter

router_v2 = APIRouter()

@router_v2.get(
  "/hello-world",
  status_code=201,
  tags=["Hello world 2"]
)
def read_root():
  return { "Hello": "World V2" }
