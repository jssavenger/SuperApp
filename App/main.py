from fastapi import FastAPI, HTTPException, status

# Creates FastAPI object 
app = FastAPI(
    title="Super App",
    description="We download apps for our needs but why we download different app for different needs. I decided fix this problem.",
    version="0.01"
)

# Creates Healthy API
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
        HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong somethink...")