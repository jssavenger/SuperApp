from fastapi import FastAPI

# Creates FastAPI object 
app = FastAPI()

# Creates Healthy API
@app.get("/", tags=['Healthy'])
async def healthy_check():
    """Healthy Check API
            Args:
                return (dict): status | messages
                return_type (dict): Python dict.
    """
    return {
        "status": True,
        "messages": "Application is healthy."
    }