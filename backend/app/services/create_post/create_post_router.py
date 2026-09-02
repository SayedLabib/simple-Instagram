from fastapi import APIRouter, Depends, Request, UploadFile ,File,HTTPException
from sqlalchemy.orm.session import Session
from app.services.create_post.create_post_schema import createPost, showPost
from app.services.create_post.create_post import create_post
from db.database import get_db
from models.models import dbPost
import os
import uuid

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

#################################

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "images")
IMAGES_DIR = os.path.normpath(IMAGES_DIR)
os.makedirs(IMAGES_DIR, exist_ok=True)

MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB
UPLOAD_CHUNK_SIZE = 1024 * 1024  # 1 MB

@router.post("/uploadImage")

def upload_image(image: UploadFile = File(...), request:Request = None):

    extension = os.path.splitext(image.filename)[1]
    random_filename = f"{uuid.uuid4()}{extension}"

    contents = image.file.read()
    if len(contents) > MAX_IMAGE_SIZE_BYTES:
        raise HTTPException(status_code=413, detail="Image exceeds maximum allowed size of 10 MB.")

    with open(os.path.join(IMAGES_DIR, random_filename), "wb") as f:
        f.write(contents)

    return {"url": str(request.base_url) + f"images/{random_filename}" }

