### Return Schema for App

from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class ReturnSchema:
    status: bool = True
    message: str = None
    data: Optional[Any] = ""
    
@dataclass
class TokenSchema:
    access_token: str
    token_type: str