from fastapi import APIRouter
from .models import User, Session
from .schema import UserRegisterSchema
from core.database_config import get_db
from fastapi import Depends, status
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
from .models import hash_password


router = APIRouter(prefix="/account", tags=["account"])


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
