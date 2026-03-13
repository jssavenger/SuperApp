from sqlalchemy import select

# database table
from backend.src.models.user import User

async def control_user(data, db):
    """Controls user information by Database.
            Args:
                data(BaseModel):
    """
    # create a query
    stmt= select(User).where(User.username == data.username, User.password == data.password )
    # execute database query
    result= await db.execute(stmt) # this is return object
    # check data or none
    result= result.scalar_one_or_none()
    return result