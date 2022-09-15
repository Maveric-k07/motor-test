from fastapi import APIRouter
from app.models.user import Post
from app.config.database import Posts
from bson.objectid import ObjectId

PostRoutes = APIRouter()


@PostRoutes.post("/post")
async def create_post(post: Post):
    id = ObjectId()
    _post = {"_id": id, "title": post.title}
    await Posts.insert_one(_post)


@PostRoutes.get("/post")
async def get_posts():
    _posts = []
    array = Posts.find()
    print(array)
    async for post in array:
        _posts.append(post)

    return _posts
