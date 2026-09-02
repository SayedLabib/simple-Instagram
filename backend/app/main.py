from fastapi import FastAPI
from models import models
from db.database import engine
from app.services.create_user.create_user_route import router as create_user_router
from app.services.create_post.create_post_router import router as create_post_router

app = FastAPI()
app.include_router(create_user_router)
app.include_router(create_post_router)

@app.get("")
def root():
    return "Hello World"


models.Base.metadata.create_all(bind=engine)