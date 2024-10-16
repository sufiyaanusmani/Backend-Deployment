from typing import Any, Generator

from sqlalchemy.orm import Session, sessionmaker

from api.core.config import SessionLocal


def get_db() -> Generator[sessionmaker[Session], Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
