from .models import User
from sqlalchemy.orm import Session
from .schema import UserRegisterSchema, UserLoginSchema
from core.database_config import get_db
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from datetime import datetime, timezone
from .models import hash_password
from .generate_jwt_tokens import generate_jwt_access_token, generate_jwt_refresh_token
from .authentications import get_access_token


router = APIRouter(prefix="/account", tags=["account"])


# register user route
@router.post("/register")
async def user_register(data: UserRegisterSchema, db: Session = Depends(get_db)):

    user = User(
        username=data.username,
        first_name=data.first_name,
        last_name=data.last_name,
        is_mechanic=data.is_mechanic,
        registred_at=datetime.now(timezone.utc),
    )

    hashed_password = hash_password(data.password)
    user.password = hashed_password
    db.add(user)
    db.commit()
    db.refresh(user)

    return JSONResponse(
        content={"message": f"user: {user.username} created"},
        status_code=status.HTTP_201_CREATED,
    )


# login user route
@router.post("/login")
async def user_login(data: UserLoginSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter_by(username=data.username).first()

    if not user or not user.validate(data.password):
        raise HTTPException(
            detail="Invalid username or password",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    access_tokne = generate_jwt_access_token(user.id)
    refresh_token = generate_jwt_refresh_token(user.id)

    return JSONResponse(
        content={"access_token": access_tokne, "refresh_token": refresh_token},
        status_code=status.HTTP_200_OK,
    )


# get access token from refresh token
@router.post("/token/refresh")
async def refresh_token(user_id: int = Depends(get_access_token)):

    access_token = generate_jwt_access_token(user_id)

    return JSONResponse(
        content={"access_token": access_token}, status_code=status.HTTP_201_CREATED
    )
