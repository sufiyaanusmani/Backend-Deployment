from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    password: str


async def login(request: Request, credentials: LoginRequest) -> JSONResponse:
    content = {"message": "login", "username": credentials.username, "password": credentials.password}
    return JSONResponse(content=content)


async def register(request: Request, new_user: RegisterRequest) -> JSONResponse:
    content = {"message": "register", "username": new_user.username, "password": new_user.password}
    return JSONResponse(content=content)
