import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./backend/database/votaciones.db"

if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    os.makedirs(os.path.dirname(SQLALCHEMY_DATABASE_URL[10:]), exist_ok=True)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_database():
    Base.metadata.create_all(bind=engine)

# Comprueba si la base de datos existe y la crea si no existe
def check_db_exists():
    try:
        with engine.connect():
            print('Database already exists.')
    except:
        print('Creating database...')
        create_database()

check_db_exists()