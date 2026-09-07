from pydantic import BaseModel
from typing import Optional, int, str
from datetime import datetime

class commentSchema(BaseModel):
    username: str
    comment: str
    timestamp:datetime
    post_id: int


