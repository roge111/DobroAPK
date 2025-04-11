from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from DataBaseManager import DataBaseManager
from UserInfo import UserInfo
import os


db_manager = DataBaseManager()
user_info = UserInfo(db_manager)


app = FastAPI()
UPLOAD_FOLDER = 'usersImage'
@app.get('/')
def root():
    return FileResponse('frontend/main.html')


# Разрешаем запросы с Live Server (5500)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

@app.post('/upImage')
async def update_image_user(photo: UploadFile = Form(...), id: str = Form(...)):
    # Проверка расширения файла
    result = await user_info.load_image_user(id, photo)

    return result