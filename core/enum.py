from enum import Enum


class CreateReservationStatusEnum(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    repairing = "repairing"
    finished = "finished"
    cancelled = "cancelled"
