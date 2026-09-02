
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from app.services.create_post.create_post_schema import showPost
from db.database import get_db
from models.models import dbPost
from typing import List

router = APIRouter(
    prefix="/get_posts",
    tags=["get_posts"],
)


@router.get("/", response_model=List[showPost])
def get_posts(db: Session = Depends(get_db)):
    return db.query(dbPost).all()

