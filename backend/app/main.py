from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from fastapi.security import OAuth2PasswordBearer
from app.routers.lobby import lobby
from app.routers.guest import guest
from app.routers.user import user


app = FastAPI()
app.include_router(lobby.router)
app.include_router(user.router)
app.include_router(guest.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
async def get():
    return {"start_message": 'hello world'}


@app.get("/token/")
async def read_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}