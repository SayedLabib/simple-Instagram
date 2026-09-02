
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from app.services.login.login import authenticate_user
from app.auth.oauth2 import create_access_token
from db.database import get_db


router = APIRouter(

    tags=["Authentication"],
)

@router.post("/login")

def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = authenticate_user(db, username=request.username, password=request.password)
    access_token = create_access_token(data={"sub": str(user.id)})

    return {
        "access_token": access_token, 
        "token_type": "bearer"
        }
