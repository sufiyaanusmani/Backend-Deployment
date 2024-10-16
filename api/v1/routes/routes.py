from fastapi import APIRouter

import api.v1.controllers.auth as AuthController  # noqa: N812

router = APIRouter()

# /api/v1/login -> POST
router.post("/login")(AuthController.login)

# /api/v1/register -> POST
router.post("/register")(AuthController.register)

# /api/v1/users/me -> GET
router.get("/users/me")(AuthController.read_users_me)
