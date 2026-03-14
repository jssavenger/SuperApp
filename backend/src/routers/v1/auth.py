from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from typing import Annotated

# database function
from backend.src.core.database import connection

# auth schema
from backend.src.schemas.auth import UserAuth

# service layer
from backend.src.services.auth import control_user

# oauth token
from backend.src.core.security import oauth2_scheme

router=APIRouter(tags=['Auth'])

@router.post("/login")
async def user_login(data: UserAuth, token: Annotated[str, Depends(oauth2_scheme)], db: AsyncSession = Depends(connection)):
    """User Login API - Controls user login information
            Args:
                data(UserAuth): Pydantic Schema
    """
    result= await control_user(data, db)
    return result