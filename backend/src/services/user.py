from sqlalchemy import select
from fastapi import HTTPException

# logger
from backend.src.services.logger_service import logger

# model
from backend.src.models.user import User

# schema
from backend.src.schemas.user import UpdateUsername
from backend.src.schemas.return_schema import ReturnSchema

async def update_username_service(
    data: UpdateUsername,
    db):
    """Update Username Service Layer
            Args:
                data (UpdateUsername)
    """
    logger.info(f"update_username_service Function called.")
    r = ReturnSchema()
    
    logger.info(f"Came data: {data.user_id} {data.new_user_name}")
    stmt = select(User).where(User.public_id == data.user_id.strip())
    result = await db.execute(stmt)
    result = result.scalar_one_or_none()

    if not result:
        logger.warning(f"User not found: '{data.new_user_name}'")
        raise HTTPException(status_code=422, detail="User not found.")

    result.username = data.new_user_name
    await db.commit()

    logger.info(f"update_username_service Function successfull.")
    return True