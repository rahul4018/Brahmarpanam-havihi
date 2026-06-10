from app.db.base import Base
from app.db.session import engine

from app.models import User


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tables Created")