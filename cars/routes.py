from fastapi import APIRouter, Depends, status
from accounts.authentications import get_authenticated_user
from core.database_config import get_db
from .schema import CarRegisterSchema, AcceptCarRepairSchema
from sqlalchemy.orm import Session
from accounts.models import User
from fastapi.exceptions import HTTPException
from .models import Car
from shops.models import MechanicReservation


router = APIRouter(prefix="/cars", tags=["cars"])


# this route will register the user cars
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


# this route will show the list of user cars
@router.get("/list")
async def cars_list_route(
    db: Session = Depends(get_db), user_id: int = Depends(get_authenticated_user)
):
    cars = db.query(Car).filter_by(user_id=user_id).all()
    return cars


@router.post("/accept-repair/{reservation_id}")
async def accept_repair_route(reservation_id: int, data: AcceptCarRepairSchema, db: Session = Depends(get_db), user_id: int = Depends(get_authenticated_user)):
    
    reservation = db.query(MechanicReservation).filter_by(id = reservation_id).first()
    
    if not reservation.user_id == user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="only reservation owner can user this route",
        )
    
    if not reservation.status == "finished":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="repairing not finished",
        )
    
    if reservation.status == "received":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="this reservation is closed",
        )
    
    if data.repaired == True:
        reservation.status = "received"
        reservation.rating = data.rating
        
        db.commit()
        db.refresh(reservation)
        
        return {"message": "your confirmation and rating registred"}
    
    reservation.status = "returned"
    db.commit()
    db.refresh(reservation)
    
    return {"message": "your reservation was returned"}