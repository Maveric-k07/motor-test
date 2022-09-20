import motor.motor_asyncio

MONGO_URL = "mongodb://localhost:27017/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

db_user = client["user-db"]
Users = db_user.get_collection("users")

db_post = client["post-db"]
Posts = db_post.get_collection("posts")