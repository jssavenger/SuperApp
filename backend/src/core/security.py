from fastapi.security import OAuth2PasswordBearer

# Create a oauth2_scheme
oauth2_scheme= OAuth2PasswordBearer(tokenUrl="/api/v1/login")