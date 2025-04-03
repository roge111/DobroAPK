from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from UserInfo import UserInfo
from DataBaseManager import DataBaseManager

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("frontend/personalAccount.html")
 


# Разрешаем запросы с Live Server (5500)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)
db_manager = DataBaseManager()
user_info = UserInfo(db_manager)


@app.post("/updateInformationAccount")
async def update_information(data: dict = Body):
    id = data.get("user_id")
    login = data.get("login")
    lfp = data.get("lfp")
    contacts = data.get("contacts")
    info = data.get("info")
    hobbi = data.get("hobbi")

    
    result = user_info.update_user(id,lfp, login, info, contacts, hobbi)
    return result

