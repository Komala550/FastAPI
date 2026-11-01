from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. import model,schemas
from ..database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from ..utils import *

router = APIRouter(prefix='/users',tags=['Users'])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_users(user : schemas.UserCreate,db : Session = Depends(get_db)):


    hashed_password = hash(user.password)
    user.password = hashed_password
    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id : int ,response :Response,db : Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id)))
    # post = cursor.fetchone()
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} was not found")

    return user