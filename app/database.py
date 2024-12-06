from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
from psycopg.rows import dict_row
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()


# db_config = {
#     'host': 'localhost',
#     'dbname': 'fastapi',
#     'user': 'postgres',
#     'password': 'shalom1023'
# }


# while True:

#     try:
#         with psycopg.connect(**db_config) as conn:
#             with conn.cursor(row_factory=dict_row) as cur:
#                 print("Database connection was successful!")
#                 break
#     except Exception as error:
#         print("Connecting to the database failed")
#         print("Error:", error)
#         time.sleep(2) 