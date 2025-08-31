from enum import Enum


class CreateReservationStatusEnum(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    repairing = "repairing"
    finished = "finished"
    cancelled = "cancelled"


class CarRepairRatingEnum(int, Enum):
    
    bad = 1
    normal = 2
    good = 3
    very_good = 4
    perfect = 5