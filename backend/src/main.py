from fastapi import FastAPI, HTTPException, status, Depends
from contextlib import asynccontextmanager
from typing import AsyncIterable
from fastapi.middleware.cors import CORSMiddleware

# Routers
from backend.src.routers.api_v1 import router as Router_v1

# SQLAlchemy Base Class
from backend.src.core.database import create_table
# tables
from backend.src.models.user import User

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterable[dict]:
    # code to run on stup
    await create_table()
    print("Tables function")
    yield

# Creates FastAPI object 
app = FastAPI(
    title="Super App",
    description="We download apps for our needs but why we download different app for different needs. I decided fix this problem.",
    version="0.01",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creates App Healthy API
@app.get("/", tags=['Healthy'])
async def healthy_check():
    """Healthy Check API
            Args:
                return (dict): status | messages
                return_type (dict): Python dict.
    """
    try:
        return {
            "status": True,
            "messages": "Application is healthy."
        }
    except:
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="App isn't healthy!")
        
# Add a routers
app.include_router(Router_v1)