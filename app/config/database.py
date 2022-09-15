import motor.motor_asyncio

MONGO_URL = "mongodb://localhost:27017/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

db = client["user-db"]
Users = db.get_collection("users")

db = client["post-db"]
Posts = db.get_collection("posts")
