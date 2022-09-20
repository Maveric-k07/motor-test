import uuid
from fastapi import APIRouter
from app.models.user import Post, User
from app.config.database import Posts, Users
from bson.objectid import ObjectId

from app.schemas.user import userEntity

UserRoutes = APIRouter()


@UserRoutes.get("/")
async def get_users():
    users = [userEntity(user) async for user in Users.find()]
    return users


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
    _ = await Users.insert_one(_user)
