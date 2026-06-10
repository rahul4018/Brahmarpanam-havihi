from jose import JWTError
from jose import jwt

from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.user import User
from app.core.config import settings


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:

        print("\n" + "=" * 50)
        print("TOKEN RECEIVED:")
        print(token)

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        print("JWT PAYLOAD:")
        print(payload)

        email = payload.get("sub")

        print("JWT EMAIL:")
        print(email)

        print("=" * 50 + "\n")

        if email is None:
            raise credentials_exception

    except JWTError as e:

        print("\nJWT ERROR:")
        print(str(e))
        print()

        raise credentials_exception

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if user is None:

        print(
            f"User not found for email: {email}"
        )

        raise credentials_exception

    return user