from pydantic import BaseModel, Field

class UserAuth(BaseModel):
    username: str = Field(default=str, min_length=10, max_length=30, description="User username.")
    password: str = Field(default=str, min_length=15, max_length=30, description="User password.")