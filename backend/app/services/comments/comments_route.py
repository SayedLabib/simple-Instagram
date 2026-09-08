from fastapi import APIRouter, Depends

from app.services.comments.comments_schema import commentBase
from app.services.comments.comments import post_comment
from sqlalchemy.orm import Session

from db.database import get_db

from app.auth.oauth2 import get_current_user
from app.services.login.login_schema import userAuth
from models.models import dbComment, dbPost


router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)


@router.get('/get_comments/{post_id}')

async def get_post_comments(post_id: int, db: Session = Depends(get_db)):
    comments = db.query(dbComment).filter(dbComment.post_id == post_id).all()
    return comments


@router.post("")
async def create_comment(comment: commentBase, db: Session = Depends(get_db), current_user: userAuth = Depends(get_current_user)):
    return post_comment(db, comment)