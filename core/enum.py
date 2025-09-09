from enum import Enum


# enum for reservation status
class CreateReservationStatusEnum(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    repairing = "repairing"
    finished = "finished"
    cancelled = "cancelled"


# enum for rating
class CarRepairRatingEnum(int, Enum):
    
    bad = 1
    normal = 2
    good = 3
    very_good = 4
    perfect = 5