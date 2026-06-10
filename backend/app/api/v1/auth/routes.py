from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.schemas.user import (
    UserRegister,
    UserResponse
)

from app.services.user_service import (
    UserService
)

from app.schemas.user import (
    UserLogin,
    TokenResponse
)

from app.core.jwt import (
    create_access_token
)

from app.api.dependencies import (
    get_current_user
)

from app.models.user import User

from app.api.permissions import (
    require_role
)

from app.constants.roles import (
    Roles
)
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = (
        UserService.get_user_by_email(
            db,
            user_data.email
        )
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = UserService.create_user(
        db,
        user_data
    )

    return user

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):

    user = (
        UserService.authenticate_user(
            db,
            credentials.email,
            credentials.password
        )
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(
    current_user: User = Depends(
        get_current_user
    )
):

    return {
        "id": current_user.id,
        "name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role
    }

@router.get("/token-test")
def token_test(
    current_user: User = Depends(
        get_current_user
    )
):
    return {
        "message": "Token Valid",
        "email": current_user.email,
        "role": current_user.role
    }

@router.get("/admin-test")
def admin_test(
    current_user=Depends(
        require_role(
            [Roles.ADMIN]
        )
    )
):

    return {
        "message": "Admin Access Granted"
    }