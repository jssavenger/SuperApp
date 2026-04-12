from pydantic import BaseModel, Field

# bearer
class Token(BaseModel):
    access_token: str
    token_type: str

class UserAuth(BaseModel):
    username: str = Field(..., min_length=10, max_length=30, description="User username.")
    password: str = Field(..., min_length=15, max_length=30, description="User password.")
    
class UserRegister(BaseModel):
    username: str = Field(..., min_length=10, max_length=30, description="User username.")
    password: str = Field(..., min_length=15, max_length=30, description="User password.")
    phone:    str = Field(..., min_length=8, max_length=16, description="User phone number.")
    email:    str = Field(..., min_length=10, max_length=40, description="User email.")
    age:      int = Field(..., description="User age.")
    hobbies: list = Field(default=list)
    