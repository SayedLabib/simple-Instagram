
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth.oauth2 import get_current_user
from db.database import get_db
from app.services.delete_post.delete_post import delete_post

router = APIRouter(
    prefix="/delete",
    tags=["delete"],
    responses={404: {"description": "Not found"}}
    )


@router.delete("/{post_id}")
def delete_route(post_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    return delete_post(db, post_id, current_user)