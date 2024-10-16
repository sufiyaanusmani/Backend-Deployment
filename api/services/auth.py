from typing import Any, Literal

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from api.constants.auth import ALGORITHM, oauth2_scheme
from api.core.config import Config
from api.models.models import User
from api.utils.auth import verify_password


def get_user_by_username(db: Session, username: str) -> (User | None):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str) -> (User | None):
    return db.query(User).filter(User.email == email).first()

def authenticate_user(db: Session, username: str, password: str) -> (User | Literal[False]):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict[str, Any | str]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception  # noqa: B904

    return {"username": username}
