from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{username}/{age}")
#async def get_user_data(username: str, age: int) -> dict:
async def get_user_data(username: Annotated[str, Path(..., min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                        age: Annotated[int, Path(..., ge=18, le=120, description="Enter age", example=24)]) -> dict:
    return {"Имя": username, "Возраст": age}


@app.get("/user/{user_id}")
async def get_user(user_id: Annotated[int, Path(..., ge=1, le=100, title="User ID", description="Enter User ID", example=1)]) -> dict:
    return {"user_id": f"Вы вошли как пользователь № {user_id}"}
