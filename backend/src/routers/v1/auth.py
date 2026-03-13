from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# database function
from backend.src.core.database import connection

# auth schema
from backend.src.schemas.auth import UserAuth

# service layer
from backend.src.services.auth import control_user

router=APIRouter(tags=['Auth'])

@router.post("/login")
async def user_login(data: UserAuth, db: AsyncSession = Depends(connection)):
    """User Login API - Controls user login information
            Args:
                data(UserAuth): Pydantic Schema
    """
    result= await control_user(data, db)
    return result