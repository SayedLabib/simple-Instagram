from db.database import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class dbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    items = relationship("dbPost", back_populates="user")
class dbPost(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("dbUser", back_populates="items")
    comments = relationship("dbComment", back_populates="post")



class dbComment(Base):
    __tablename__ = "comments"

    id= Column(Integer, primary_key=True, index=True)
    username = Column(String)
    comment = Column(String)
    timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("dbPost", back_populates="comments")