from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from typing import Annotated, Optional
from fastapi.security import OAuth2PasswordRequestForm

# logger
from backend.src.services.logger_service import logger

# database function
from backend.src.core.database import connection

# auth schema
from backend.src.schemas.auth import UserAuth, UserRegister

# return schema
from backend.src.schemas.return_schema import ReturnSchema, TokenSchema

# service layer
from backend.src.services.auth import control_user
from backend.src.services.auth import user_register_service

# oauth token
from backend.src.core.security import oauth2_scheme

router=APIRouter(tags=['Auth'])

@router.post("/login")
async def user_login(
    data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(connection)
    ) -> Optional[ReturnSchema | TokenSchema]:
    """User Login API - Controls user login information
            Args:
                data(UserAuth): Pydantic Schema
    """
    logger.info(f"/login API called.")
    
    response= ReturnSchema()
    
    logger.info(f"control_user calling...")
    result= await control_user(data, db)
    
    if not result.status:
        logger.warning(f"control_user status isn't true.")
        response.status= False
        return response
    
    
    logger.info(f"control_user status is true.")
    response= TokenSchema(
        access_token="123",
        token_type="Bearer"
    )
    
    return response

@router.post("/register")
async def user_register(
    data: UserRegister,
    db: AsyncSession = Depends(connection)):
    """Registers a new users
            Args:
                data (UserAuth): Pydantic Schema
    """
    logger.info(f"user_register API called.")
    
    response = ReturnSchema()
    
    r = await user_register_service(data, db)
    
    return r