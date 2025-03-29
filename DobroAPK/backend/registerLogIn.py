import psycopg2
import bcrypt
from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from DataBaseManager import DataBaseManager
from UserService import UserService
 
app = FastAPI()


 
@app.get("/")
def root():
    return FileResponse("frontend/index.html")
 


# Разрешаем запросы с Live Server (5500)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


db_manager = DataBaseManager()
user_service = UserService(db_manager)



@app.post("/register")
async def register(data: dict = Body()):
    log = data.get("name")
    pswd = data.get("pswd")
    success = user_service.register(log, pswd)
    return success

@app.post("/login")
async def logIn(data: dict = Body):
    log = data.get("name")
    pswd = data.get("pswd")
    success = user_service.login(log, pswd)
    return success



    