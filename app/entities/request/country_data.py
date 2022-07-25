from pydantic import BaseModel

class CountryData(BaseModel):
    cat_region: int
    score: float
    gdp: float
    social_support: float
    freedom: float
    generosity: float
    corruption: float
    positive_affect: float
    negative_affect: float
    hle: float