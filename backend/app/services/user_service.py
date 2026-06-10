from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserRegister
from app.core.security import hash_password
from app.core.security import verify_password


class UserService:

    @staticmethod
    def get_user_by_email(
        db: Session,
        email: str
    ):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def create_user(
        db: Session,
        user_data: UserRegister
    ):

        hashed_password = hash_password(
            user_data.password
        )

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            phone=user_data.phone,
            password_hash=hashed_password,
            role="customer"
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user
    @staticmethod

    def authenticate_user(
        db: Session,
        email: str,
        password: str
        ):
        
        user = (
            UserService.get_user_by_email(
                db,
                email
            )
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash
        ):
            return None

        return user