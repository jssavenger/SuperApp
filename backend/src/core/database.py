# Database engine, session
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import  declarative_base
from sqlalchemy import create_engine
from pathlib import Path
from dotenv import load_dotenv
import os

# file paths
_CURRENT_PATH=Path(__file__).parent.parent.parent.parent
_ENV_PATH=_CURRENT_PATH/".env"

# load .env file 
load_dotenv(dotenv_path=_ENV_PATH)

# database information
_POSTGRES_DB=os.getenv("POSTGRES_DB")
_POSTGRES_USER=os.getenv("POSTGRES_USER")
_POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")

# database url
_DATABASE_URL= f"postgresql+asyncpg://{_POSTGRES_USER}:{_POSTGRES_PASSWORD}@db:5432/{_POSTGRES_DB}"

# Create a Base Class
Base=declarative_base()
# Create an engine
engine=create_async_engine(_DATABASE_URL)
# Create a SessionLocal class (sessionmaker)
# autocommit=False : Islemlerin veritabanina otomatik kaydedilmesini engeller, commit gerekir.
# autofluch=False  : Islemlerin veritabanina sorgu gitmeden once otomatik yansimasini engeller.
SessionLocal=async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# Create a Session instance
session=SessionLocal()

# create a database connection and share session 
async def connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# create database tables
async def create_table():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Table created")
    except Exception as e:
        print("Error: ", str(e))