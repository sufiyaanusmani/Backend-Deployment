import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./eyecon.db"

    SECRET_KEY = os.getenv("SECRET_KEY")

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


