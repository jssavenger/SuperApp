from sqlalchemy import select
from typing import Optional

# database table
from backend.src.models.user import User

# return schema
from backend.src.schemas.return_schema import ReturnSchema

# logger
from backend.src.services.logger_service import logger

async def control_user(data, db) -> Optional[ReturnSchema]:
    """Controls user information by Database.
            Args:
                data(BaseModel):
    """
    response= ReturnSchema()
    
    # create a query
    stmt= select(User).where(User.username == data.username, User.password == data.password )
    # execute database query
    result= await db.execute(stmt) # this is return object
    # check data or none
    result= result.scalar_one_or_none()
    logger.info(f"Database result came.")
    
    if not result:
        response.status= False
        return response
    
    logger.info(f"Database result isn't None.")
    response.data= result.username
    return response