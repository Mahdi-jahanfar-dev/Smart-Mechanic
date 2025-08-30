from enum import Enum


class CreateReservationStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    repairing = "repairing"
    finished = "finished"
    cancelled = "cancelled"
