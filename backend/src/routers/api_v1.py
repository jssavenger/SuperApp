from fastapi import APIRouter, HTTPException, status

# Version 1 routers
from backend.src.routers.v1.auth import router as UserLoginRouter

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(UserLoginRouter)

# Creates App Version 1 Healtyh API
@router.get("/", tags=['Healthy'])
async def healthy_check():
    """Healthy Check API
            Args:
                return (dict): status | messages
                return_type (dict): Python dict.
    """
    try:
        return {
            "status": True,
            "messages": "Application version 1 is healthy."
        }
    except:
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="App version 1 isn't healthy!")