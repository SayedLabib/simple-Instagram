from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from app.services.create_post.create_post_schema import createPost, showPost
from app.services.create_post.create_post import create_post
from db.database import get_db
from models.models import dbPost

router = APIRouter(
    prefix="/create_post",
    tags=["create_post"],
)


image_url_type = ["url", "base64"]


@router.post("/", response_model=showPost)
def Create_post(post: createPost, db: Session = Depends(get_db)):
    if post.image_url_type not in image_url_type:
        raise HTTPException(status_code=422, detail="Unprocessable image_url_type. Must be 'url' or 'base64'.")

    new_post = create_post(db, post)
    return new_post

