# from fastapi import FastAPI, Body
# from fastapi.responses import FileResponse, JSONResponse
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Разрешаем запросы с Live Server (5500)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://127.0.0.1:5500"],  # Точный адрес Live Server
#     allow_methods=["POST"],
#     allow_headers=["Content-Type"],
# )

# @app.post("/hello")
# async def hello(data: dict = Body(...)):
#     name = data["name"]
#     age = data["pswd"]
#     return {"message": f"{name}, ваш возраст - {age}"}