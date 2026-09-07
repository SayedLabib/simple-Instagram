from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.models import dbPost
from models.models import dbUser


def delete_post(db: Session, post_id: int, current_user: dbUser):
    post = db.query(dbPost).filter(dbPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")
    db.delete(post)
    db.commit()
    return {"detail": "Post deleted successfully"}