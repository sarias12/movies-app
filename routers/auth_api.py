# FastAPI
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# JWT
from jwt_manager import create_token

# Data Validation - Pydantic
from schemas import User

router = APIRouter()


@router.post("/login", tags=["Auth"])
def login(user: User):
    if user.user == "test" and user.password == "password":
        tk: str = create_token(user.dict())
    return JSONResponse(status_code=200, content=tk)
