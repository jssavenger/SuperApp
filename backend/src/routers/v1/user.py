from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# logger
from backend.src.services.logger_service import logger

# database function
from backend.src.core.database import connection

# Token security
from backend.src.core.security import oauth2_scheme

# return schema
from backend.src.schemas.return_schema import ReturnSchema

# schema
from backend.src.schemas.user import UpdateUsername

# service
from backend.src.services.user import update_username_service

router = APIRouter(
    tags=["User Process"]
)

@router.post("/update-username")
async def update_username(
    data: UpdateUsername,
    db: AsyncSession = Depends(connection),
    token: str = Depends(oauth2_scheme)) -> ReturnSchema:
    """Username Update API
            Args:
                data (UpdateUsername): Pydantic Schema
                token: Bearer token
    """
    logger.info(f"update_username API called.")
    r = ReturnSchema()

    response = await update_username_service(data, db)

    r.data = response
    return r