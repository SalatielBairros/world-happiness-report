from decimal import Decimal
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base  = declarative_base()

class NintendoSwitch(Base):
  __tablename__ = 'nintendo_switch'

  id = Column(Integer, primary_key=True, index=True)
  store_name = Column(String)
  product_name = Column(String)
  price = Column(Decimal)
  time_created = Column(DateTime(timezone=True), server_default=func.now())
