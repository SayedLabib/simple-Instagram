from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from app.services.create_user.create_user_schema import CreateUser, ShowUser
from app.services.create_user.create_user import create_user as create_user_service
from db.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/create", response_model=ShowUser)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    db_user = create_user_service(db, user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return db_user 