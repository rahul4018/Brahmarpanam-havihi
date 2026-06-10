from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base


class ServiceCategory(Base):

    __tablename__ = "service_categories"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name_en: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    name_kn: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    slug: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )