from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from accounts.authentications import get_authenticated_user
from accounts.models import User
from .schema import MechanicShopsListSchema, MechanicCreateSchema
from typing import List
from sqlalchemy.orm import Session
from .models import MechanicShop
from core.database_config import get_db
from sqlalchemy.exc import IntegrityError  # using for unique errors in db


router = APIRouter(prefix="/shops", tags=["mechanic-shops"])


@router.get("/list", response_model=List[MechanicShopsListSchema])
async def shops_list(
    db: Session = Depends(get_db), user_id: int = Depends(get_authenticated_user)
):
    shops = db.query(MechanicShop).all()
    return shops


@router.post("/create")
async def create_mechanic_shop(
    data: MechanicCreateSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_authenticated_user),
):
    user = db.query(User).filter_by(id=user_id).first()
    if user.is_mechanic:
        mechanic_shop = MechanicShop(**data.model_dump())
        try:
            mechanic_shop.user_id = user_id
            db.add(mechanic_shop)
            db.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="mechanic with this user is already exist",
            )
        except Exception as e:
            return {"error": e}

        return {"message": f"mechanic: {mechanic_shop.name} created"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="only mechanics can create mechanic shop",
    )
