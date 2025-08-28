from fastapi import APIRouter, Depends, status
from accounts.authentications import get_authenticated_user
from core.database_config import get_db
from .schema import CarRegisterSchema
from sqlalchemy.orm import Session
from accounts.models import User
from fastapi.exceptions import HTTPException
from .models import Car


router = APIRouter(prefix="/cars", tags=["cars"])


@router.post("/register")
async def car_register(
    data: CarRegisterSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_authenticated_user),
):
    user = db.query(User).filter_by(id=user_id).first()

    if user.is_mechanic:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="only normal users can register car",
        )

    car = Car(**data.model_dump())

    car.user_id = user_id

    db.add(car)
    db.commit()

    return {"message": f"car {car.model} registred successfully"}
