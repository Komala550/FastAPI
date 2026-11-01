from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
from urllib.parse import quote_plus

password = quote_plus(settings.database_password)

SQL_ALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{settings.database_username}:"
    f"{password}@{settings.database_hostname}:"
    f"{settings.database_port}/{settings.database_name}"
)
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost' , database = 'fastapi' , user = 'postgres' , password = 'Postgres@18$$0' , cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection successful")
#         break

#     except Exception as error:
#         print("Connecting to DB failed")
#         print("Error:",error)
#         time.sleep(2)

