from pydantic import BaseModel
from datetime import datetime

class commentBase(BaseModel):
    username: str
    comment: str
    post_id: int


