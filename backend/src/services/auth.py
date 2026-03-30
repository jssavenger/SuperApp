from sqlalchemy import select
from typing import Optional
import bcrypt
from fastapi import HTTPException

# database table
from backend.src.models.user import User

# return schema
from backend.src.schemas.return_schema import ReturnSchema

# pydantic schema
from backend.src.schemas.auth import UserRegister

# logger
from backend.src.services.logger_service import logger

async def control_user(data, db) -> Optional[ReturnSchema]:
    """Controls user information by Database.
            Args:
                data(BaseModel):
    """
    response= ReturnSchema()
    
    stmt   = select(User).where(User.username == data.username)
    result = await db.execute(stmt)
    result = result.scalar_one_or_none()
    if not result:
        logger.warning(f"User not found: '{data.username}'")
        raise HTTPException(status_code=422, detail="User not found.")
    
    if not bcrypt.checkpw(data.password.encode('utf-8'), result.password.encode('utf-8')):
        logger.warning(f"User password isn't true: '{data.username}'")
        raise HTTPException(status_code=422, detail="Password isn't true.")
    
    logger.info(f"Database result isn't None.")
    response.data= result.username
    return response

async def user_register_service(data: UserRegister, db) -> Optional[ReturnSchema]:
    """Registers user service
            Args:
                data (UserRegister): Pydantic schema
                db   (AsyncSession): Database session
    """
    response = ReturnSchema()
    
    try:
        pw = data.password.encode('utf-8')
        s  = bcrypt.gensalt()
        h  = bcrypt.hashpw(pw, s).decode("utf-8")
        
        new_user = User(
            username=data.username,
            password=h,
            phone=data.phone,
            email=data.email,
            age=data.age,
            hobbies=data.hobbies
        )
        
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        
        response.message = f"User registered.\nUsername: '{data.username}'"
    except Exception as e:
        logger.error(f"Error from user register: {str(e).strip()}")
        response.status = False
        response.message= f"Error from user registered: {str(e).strip()}"
    
    return response
    