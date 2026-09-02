from .create_user_schema import CreateUser
from sqlalchemy.orm.session import Session
from app.auth.hash import Hash

from models.models import dbUser


def create_user(db: Session, user: CreateUser):
    new_user = dbUser(
        username=user.username,
        email=user.email,
        password=Hash.bcrypt(user.password)  # We need to Hash the password through JWT
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user