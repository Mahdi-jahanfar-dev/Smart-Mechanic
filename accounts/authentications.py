from fastapi import Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.exceptions import HTTPException
import jwt
from core.config import settings
from jwt import exceptions as jexceptions


security = HTTPBearer()


def get_authenticated_user(
    cerdential: HTTPAuthorizationCredentials = Depends(security),
) -> int:

    token = cerdential.credentials

    try:
        decoded_token = jwt.decode(
            token, key=settings.JWT_SECRET_KEY, algorithms=["HS256"]
        )

        if decoded_token["type"] == "access":

            user_id = decoded_token["user_id"]
            return user_id

        raise HTTPException(detail="token type is not access")

    except jexceptions.ExpiredSignatureError:
        raise HTTPException(
            detail="Token expired", status_code=status.HTTP_401_UNAUTHORIZED
        )
    except jexceptions.DecodeError:
        raise HTTPException(
            detail="Decode faild", status_code=status.HTTP_401_UNAUTHORIZED
        )
    except jexceptions.InvalidTokenError:
        raise HTTPException(
            detail={"Invalid Token"}, status_code=status.HTTP_401_UNAUTHORIZED
        )


def get_access_token(
    credential: HTTPAuthorizationCredentials = Depends(security),
) -> int:

    token = credential.credentials

    try:
        decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])

        if decoded_token["type"] != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type"
            )

        user_id = decoded_token["user_id"]
        return user_id

    except jexceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="expired token"
        )

    except jexceptions.InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid signature"
        )

    except jexceptions.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
