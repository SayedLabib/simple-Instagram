from sqlalchemy.orm import Session
from models.models import dbComment
from datetime import datetime
from app.services.comments.comments_schema import commentBase


def post_comment(db:Session, comment:commentBase):

    new_comment = dbComment(
        username=comment.username,
        comment=comment.comment,
        post_id=comment.post_id,
        timestamp=datetime.now()
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

    
def get_comments(db:Session, post_id:int):
    return db.query(dbComment).filter(dbComment.post_id == post_id)