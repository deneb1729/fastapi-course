from pydantic import BaseModel
from typing import List, Optional


class Blog(BaseModel):
    title: str
    body: str


class BlogList(Blog):

    class Config():
        orm_mode = True


class BaseUser(BaseModel):
    name: str
    email: str


class User(BaseUser):
    password: str


class UserOut(BaseUser):
    blogs: List[BlogList]

    class Config():
        orm_mode = True


class Creator(BaseUser):
    class Config():
        orm_mode = True


class BlogOut(Blog):
    creator: Creator

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

