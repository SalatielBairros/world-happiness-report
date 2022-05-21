from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

host = getenv('DB_HOST')
username = getenv('POSTGRES_USER')
password = getenv('POSTGRES_PASSWORD')
database = getenv('POSTGRES_DB')

sqlalchemy_database_url = (
  "postgresql://{user}:{pwd}@{host}/{db}".format(
    user=username,
    pwd=password,
    host=host,
    db=database
  )
)

engine = create_engine(sqlalchemy_database_url, echo=False)

SessionLocal = sessionmaker(
  autocommit=False, autoflush=False, bind=engine
)
