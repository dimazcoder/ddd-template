from fastapi import FastAPI
from app.routes import user_router, home_router

app = FastAPI()

app.include_router(user_router)
app.include_router(home_router)