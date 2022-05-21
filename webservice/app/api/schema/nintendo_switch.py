from datetime import datetime

from pydantic import BaseModel

class NintendoSwitch(BaseModel):

  id: int
  store_name: str
  product_name: str
  price: float
  time_created: datetime
