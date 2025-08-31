from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from accounts.authentications import get_authenticated_user
from accounts.models import User
from .schema import (
    MechanicShopsListSchema,
    MechanicCreateSchema,
    MechanicDetailSchema,
    MechanicResevationCreateSchema,
    MechanicChooseStatusSchema,
)
from typing import List
from sqlalchemy.orm import Session
from .models import MechanicShop, MechanicReservation
from core.database_config import get_db
from sqlalchemy.exc import IntegrityError  # using for unique errors in db
from cars.models import Car


router = APIRouter(prefix="/shops", tags=["mechanic-shops"])


# this route will return list of mechanic shops
@router.get("/list", response_model=List[MechanicShopsListSchema])
async def shops_list(
    db: Session = Depends(get_db), user_id: int = Depends(get_authenticated_user)
):
    shops = db.query(MechanicShop).all()
    return shops


# this route will return mechanic detail
@router.get("/{shop_id}", response_model=MechanicDetailSchema)
async def shop_detail(
    shop_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_authenticated_user),
):
    shop = db.query(MechanicShop).filter_by(id=shop_id).first()
    if not shop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="shop not found"
        )
    return shop


# this route will create mechanic shop if user.is_mechanic
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


# this route create a reservation for users
@router.post("/reservation/registration")
async def resevation_create_route(
    data: MechanicResevationCreateSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_authenticated_user),
):
    reservation = MechanicReservation(**data.model_dump())
    car = db.query(Car).filter_by(user_id=user_id).first()
    if not car:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="just car owner can register resevation",
        )

    date_exist = db.query(MechanicReservation).filter_by(date=data.date).first()

    if date_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="This time is booked"
        )

    reservations = (
        db.query(MechanicReservation)
        .filter(
            MechanicReservation.car_id == data.car_id,
            MechanicReservation.status.notin_(["cancelled", "finished"]),
        )
        .first()
    )
    if reservations:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="this car is already in mechanic shop",
        )

    reservation.user_id = user_id
    reservation.status = "pending"

    db.add(reservation)
    db.commit()

    return {
        "message": f"Your mechanic shop reservation for date:{reservation.date} has been registered status : pending"
    }


# this route will show the reservation list for each mechanic shop
@router.get("/resevations/{shop_id}")
async def resevation_list_route(
    shop_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_authenticated_user),
):
    resevations = db.query(MechanicReservation).filter_by(shop_id=shop_id).all()

    return resevations


# this route will change reservation status
@router.post("/reservation/status/{reservation_id}")
async def reservation_choose_status_route(
    reservation_id: int,
    data: MechanicChooseStatusSchema,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_authenticated_user),
):
    user = db.query(User).filter_by(id=user_id).first()
    if not user.is_mechanic:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="only mechanics can change reservation status",
        )

    reservation = db.query(MechanicReservation).filter_by(id=reservation_id).first()

    if not reservation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="reservation with this detail not found",
        )

    if not user.mechanic_shop.id == reservation.shop_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="only mechanic shop owner can change reservation status",
        )

    reservation.status = data.status

    db.commit()
    db.refresh(reservation)

    return {"message": "reservation status updated"}


@router.get("/user/reservations")
async def user_reservations_list(db: Session = Depends(get_db), user_id: int = Depends(get_authenticated_user)):
    
    user = db.query(User).filter_by(id = user_id).first()
    
    if user.is_mechanic:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="only normal users can use this route",
        )
        
    reservations = db.query(MechanicReservation).filter_by(user_id = user_id).all()
    
    return reservations