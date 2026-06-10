from sqlalchemy import text

from app.db.session import engine


try:
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT 1")
        )

        print("Database Connected")
        print(result.scalar())

except Exception as e:
    print(e)