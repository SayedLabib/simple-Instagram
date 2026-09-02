from pydantic import BaseModel


class userAuth(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


