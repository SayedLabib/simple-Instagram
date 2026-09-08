from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.models import dbUser



def delete_user(db: Session, user_id: int):
    user = db.query(dbUser).filter(dbUser.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}