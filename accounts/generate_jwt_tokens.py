import jwt
from datetime import datetime, timezone, timedelta
from core.config import settings


def generate_jwt_access_token(user_id: int, exp_time: int = 30) -> str:

    now = datetime.now(timezone.utc)

    payload = {
        "type": "access",
        "user_id": user_id,
        "iat": now,
        "exp": now + timedelta(minutes=30),
    }

    access_token = jwt.encode(payload, key=settings.JWT_SECRET_KEY, algorithm="HS256")
    return access_token


def generate_jwt_refresh_token(user_id: int, exp_time: int = 1) -> str:

    now = datetime.now(timezone.utc)

    payload = {
        "type": "refresh",
        "user_id": user_id,
        "iat": now,
        "exp": now + timedelta(days=30),
    }

    refresh_token = jwt.encode(payload, key=settings.JWT_SECRET_KEY, algorithm="HS256")
    return refresh_token
