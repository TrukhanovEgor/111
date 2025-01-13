from fastapi import FastAPI

# Создаем экземпляр приложения FastAPI
app = FastAPI()


# "Главная страница".
@app.get( "/" )
async def read_root() -> dict:
    return {"message": "Главная страница"}


@app.get( "/user/admin" )
async def read_admin() -> dict:
    return {"message": "Вы вошли как адмистратор"}


@app.get( "/user/{user_id}" )
async def get_user(user_id: int) -> dict:
    return {"user_id": f"Вы вошли как пользователь № {user_id}, "}


@app.get( "/user/{username}/{age}" )
async def get_user_data(username: str, age: int) -> dict:
    return {"Имя": username, "Возраст": age}
