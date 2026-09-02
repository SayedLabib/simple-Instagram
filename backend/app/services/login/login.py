
from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from app.auth.hash import Hash
from models.models import dbUser


def get_user_by_username(db: Session, username: str):
    return db.query(dbUser).filter(dbUser.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(dbUser).filter(dbUser.id == user_id).first()


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not Hash.verify(user.password, password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
    return user