from pydantic import BaseModel
from datetime import datetime

from typing import List

class createPost(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True

class comment(BaseModel):
    username: str
    comment: str
    timestamp: datetime

    class Config:
        orm_mode = True

class showPost(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[comment]

    class Config:
        orm_mode = True
