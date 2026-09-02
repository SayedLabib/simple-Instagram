
from datetime import datetime
from sqlalchemy.orm.session import Session
from app.services.create_post.create_post_schema import createPost
from models.models import dbPost


def create_post(db: Session, post: createPost):

    new_post = dbPost(
        image_url=post.image_url,
        image_url_type=post.image_url_type,
        caption=post.caption,
        timestamp=datetime.now(),
        user_id=post.creator_id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post