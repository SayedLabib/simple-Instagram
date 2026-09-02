from fastapi import FastAPI
from models import models
from db.database import engine
from app.services.create_user.create_user_route import router as create_user_router
from app.services.create_post.create_post_router import router as create_post_router
from app.services.create_post.create_post_router import IMAGES_DIR
from app.services.get_posts.get_posts_router import router as get_posts_router
from app.services.login.login_router import router as login_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(create_user_router)
app.include_router(create_post_router)
app.include_router(get_posts_router)
app.include_router(login_router)

@app.get("")
def root():
    return "Hello World"


models.Base.metadata.create_all(bind=engine)

app.mount("/images", StaticFiles(directory=IMAGES_DIR), name="image")