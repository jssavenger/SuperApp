# Database user table
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime
from typing import Optional, List
from sqlalchemy.dialects.postgresql import ARRAY
import datetime

# base class
from backend.src.core.database import Base

class User(Base):
    __tablename__ = "user_account"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(30), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    hobbies: Mapped[List[str] | None] = mapped_column(ARRAY(String), nullable=True) 
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.datetime.now)