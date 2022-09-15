import uuid
from fastapi import APIRouter
from app.models.user import Post, User
from app.config.database import Posts, Users
from bson.objectid import ObjectId

UserRoutes = APIRouter()


@UserRoutes.get("/")
async def get_users():
    _users = []
    array = Users.find()
    print(array)
    async for user in array:
        _users.append(user)

    return _users


@UserRoutes.post("/")
async def create_user(user: User):
    id = ObjectId()
    _user = {
        "_id": id,
        "email": user.email,
        "firstName": user.firstName,
        "lastName": user.lastName,
        "password": user.password,
    }
    await Users.insert_one(_user)
