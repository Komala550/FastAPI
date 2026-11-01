from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from typing import List,Optional
from .. import model,schemas,oauth2
from ..database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from sqlalchemy import func


router = APIRouter(prefix="/posts",tags=['Posts'])


@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user),limit : int = 10,skip :int = 0,search : Optional[str]=''):
    # cursor.execute(""" SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(model.Post).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()

    results = db.query(model.Post,func.count(model.Vote.post_id).label("votes")).join(model.Vote,model.Vote.post_id == model.Post.id, isouter = True).group_by(model.Post.id).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()
    return results

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post : schemas.PostCreate,db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """ ,(post.title , post.content , post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    print(current_user.id)

    new_post = model.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post




@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id : int ,response :Response,db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id)))
    # post = cursor.fetchone()
    post = db.query(model.Post,func.count(model.Vote.post_id).label("votes")).join(model.Vote,model.Vote.post_id == model.Post.id, isouter = True).group_by(model.Post.id).filter(model.Post.id == id).first()
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} was not found")

    return post



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id,db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    #cursor.execute("""DELETE FROM posts WHERE id = %s   RETURNING  * """,(str(id)))

    deleted_post = db.query(model.Post).filter(model.Post.id == id)

    if not deleted_post.first() :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} was not found")
    
    if deleted_post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Not auth to perform this')
    
    deleted_post.delete(synchronize_session = False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

#title str,content str,category,Bool published


@router.put("/{id}",response_model=schemas.Post)
def update_post(id : int ,post : schemas.PostCreate,db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title = %s , content = %s , published = %s where id = %s RETURNING *""", (post.title , post.content , post.published ,str(id)))
    # updated_post = cursor.fetchone()
    updated_post_query = db.query(model.Post).filter(model.Post.id == id)
    updated_post = updated_post_query.first()

    if not updated_post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} was not found")
    
    if updated_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Not auth to perform this')
    
    updated_post_query.update(post.dict(),synchronize_session = False)
    db.commit()
    db.refresh(updated_post)
    return updated_post


