from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel


# Создаем экземпляр приложения FastAPI
app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

# Определение базового маршрута
@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}

# Запрос на получение всех пользователей
@app.get('/users')
def get_users() -> List[User]:
    return users

# Запрос на добавление пользователя
@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(..., min_length=5, max_length=20, description="Enter username", examples="UrbanUser")],
                      age: Annotated[int, Path(..., ge=18, le=120, description="Enter age", examples=24)]) -> User:

    if len(users) != 0:
        new_id = len(users) + 1
    else:
        new_id = 1

    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


# Запрос на изменение данных пользователя
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(..., ge=1, le=100, title="User ID", description="Enter User ID", examples=1)],
                      username: Annotated[str, Path(..., min_length=5, max_length=20, description="Enter username", examples="UrbanUser")],
                      age: Annotated[int, Path(..., ge=18, le=120, description="Enter age", examples=24)]) -> User:

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    else:
        raise HTTPException(status_code=404, detail='Пользователя не существует')


# Запрос на удаление конкретного пользователя
@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(..., ge=1, le=100, title="User ID", description="Enter User ID", examples=1)]) -> User:

    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    else:
        raise HTTPException(status_code=404, detail='Пользователя не существует')