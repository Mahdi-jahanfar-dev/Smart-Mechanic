from fastapi import APIRouter, Depends
from accounts.authentications import get_authenticated_user
from .schema import MechanicShopsList
from typing import List
from sqlalchemy.orm import Session
from .models import MechanicShop
from core.database_config import get_db


router = APIRouter(prefix="/shops", tags=["mechanic-shops"])


@router.get("/list", response_model=List[MechanicShopsList])
async def shops_list(
    db: Session = Depends(get_db), user_id: int = Depends(get_authenticated_user)
):
    shops = db.query(MechanicShop).all()
    return shops
