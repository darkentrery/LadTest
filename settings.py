import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, Session

# class Settings(BaseSettings):
#     main_url: str
#     POSTGRES_USER: str
#     POSTGRES_PASSWORD: str
#     POSTGRES_NAME: str
#     POSTGRES_HOST: str
#     POSTGRES_PORT: str
#
#     @property
#     def SQLALCHEMY_DATABASE_URL(self):
#         return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"
#
#     @property
#     def engine(self):
#         return create_async_engine(self.SQLALCHEMY_DATABASE_URL, echo=True)
#
#     @property
#     def async_session(self):
#         return sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=False, autoflush=True)


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_NAME = os.getenv("POSTGRES_NAME")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")


# settings = Settings()

SQLALCHEMY_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"

engine = create_engine(SQLALCHEMY_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# async def init_models():
#     async with settings.engine.begin() as conn:
#         await conn.run_sync(settings.Base.metadata.drop_all)
#         await conn.run_sync(settings.Base.metadata.create_all)
#
#
# async def get_session() -> AsyncSession:
#     async with settings.async_session() as session:
#         yield session
