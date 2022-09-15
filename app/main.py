from fastapi import FastAPI
from app.routes.post import PostRoutes

from app.routes.user import UserRoutes

app = FastAPI()

app.include_router(UserRoutes)
app.include_router(PostRoutes)
