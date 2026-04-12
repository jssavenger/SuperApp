from pydantic import BaseModel, Field

class UpdateUsername(BaseModel):
    user_id: str  = Field(..., min_length=10)
    new_user_name: str = Field(..., min_length=10)