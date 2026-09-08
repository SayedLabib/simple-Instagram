from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.delete_user.delete_user import delete_user
from db.database import get_db



router = APIRouter(
    prefix="/delete_users",
    tags=["Delete_Users"]
)


@router.delete("/{user_id}")
def Delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)