from fastapi import FastAPI, Path
from typing import Annotated


users_db = {'1': {"Имя": "Example", "возраст": 18}}

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
async def get_user_data(username: Annotated[str, Path(..., min_length=5, max_length=20, description="Enter username", examples="UrbanUser")],
                        age: Annotated[int, Path(..., ge=18, le=120, description="Enter age", examples=24)]) -> dict:
    return {"Имя": username, "Возраст": age}


@app.get("/user/{user_id}")
async def get_user(user_id: Annotated[str, Path(..., title="User ID", description="Enter User ID", examples=1)]) -> dict:
    return {"user_id": f"Вы вошли как пользователь № {user_id}"}


@app.get("/users")
async def get_users() -> dict:
    return users_db


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(..., min_length=5, max_length=20, description="Enter username", examples="UrbanUser")],
                      age: Annotated[int, Path(..., ge=18, le=120, description="Enter age", examples=24)]) -> str:

    # текущий индекс = (находим номер последней строки БД и прибавляем один
    curr_ind = str(int(max(users_db, key=int)) + 1)
    users_db[curr_ind] = {"Имя": username, "возраст": age}
    return f"User {curr_ind} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(..., title="User ID", description="Enter User ID", examples='1')],
                      username: Annotated[str, Path(..., min_length=5, max_length=20, description="Enter username", examples="UrbanUser")],
                      age: Annotated[int, Path(..., ge=18, le=120, description="Enter age", examples=24)]) -> str:

    users_db[user_id] = {"Имя": username, "возраст": age}
    return f"User {user_id} has been updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(..., title="User ID", description="Enter User ID", examples=1)]) -> str:

    users_db.pop(user_id)
    return  f"User {user_id} has been deleted"