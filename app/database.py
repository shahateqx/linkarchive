from sqlalchemy import create_engine, text

from app.models import Base

DATABASE_URL = (
    "postgresql+psycopg2://"
    "linkarchive:linkarchive_dev_password@localhost:5432/linkarchive"
)

engine = create_engine(DATABASE_URL)


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar()


def create_tables():
    Base.metadata.create_all(bind=engine)