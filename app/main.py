import uvicorn
from fastapi import FastAPI

from app.api.routes.user_routes import router as post_routes

app = FastAPI()

app.include_router(post_routes)




