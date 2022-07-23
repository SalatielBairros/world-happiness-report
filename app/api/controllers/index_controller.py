from fastapi import APIRouter

router = APIRouter(prefix="")

@router.get("/", tags=["Index"])
def get_index():
    return {"message": "Welcome World Happiness Score API"}
