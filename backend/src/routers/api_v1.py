from fastapi import APIRouter, HTTPException, status

# Version 1 routers
from backend.src.routers.v1.auth import router as UserLoginRouter
from backend.src.routers.v1.user import router as UserProcessRouter
router = APIRouter(
    prefix="/api/v1",
    tags=["Version 0.1"]
)

router.include_router(UserLoginRouter)
router.include_router(UserProcessRouter)

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