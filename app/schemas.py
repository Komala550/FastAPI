from pydantic import BaseModel,EmailStr,conint,ConfigDict
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True


class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email : EmailStr
    password : str


class UserResponse(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    class Config :
        orm_mode = True


class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Post(PostBase):
    id :int
    owner_id : int
    owner : UserResponse
    created_at : datetime

    class Config :
        orm_mode = True


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    Post: Post
    votes: int

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None



class Vote(BaseModel):
    post_id :int 
    dir : conint(le=1)