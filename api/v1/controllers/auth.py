from fastapi import Depends, HTTPException, Request, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from api.models.models import User
from api.services.auth import authenticate_user, get_current_user, get_user_by_email, get_user_by_username
from api.services.db import get_db
from api.utils.auth import create_access_token, get_password_hash


class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def login(request: Request, user: LoginRequest, db: Session = Depends(get_db)) -> dict[str, str]:  # noqa: ARG001, B008
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


def register(request: Request, user: RegisterRequest, db: Session = Depends(get_db)) -> dict[str, str]:  # noqa: ARG001, B008
    db_user = get_user_by_username(db, user.username)
    db_email = get_user_by_email(db, user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    if db_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, name=user.name, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create token for the new user
    access_token = create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


def read_users_me(current_user: dict = Depends(get_current_user)) -> dict:  # noqa: B008
    return current_user
