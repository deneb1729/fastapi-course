from fastapi import APIRouter, status, HTTPException, Response, Depends
from typing import List
from blog import schemas, database, models, oauth2
from blog.repository import blog
from sqlalchemy.orm import Session


router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.post("",
          status_code=status.HTTP_201_CREATED)
def create_blog(
        request: schemas.Blog,
        db: Session = Depends(database.get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)
    ):
    return blog.create(request, db, current_user)


@router.delete("/{id}",
            status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(
        id: int,
        db: Session = Depends(database.get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)
    ):
    return blog.destroy(id, db)


@router.put("/{id}",
         status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(
        id: int,
        request: schemas.Blog,
        db: Session = Depends(database.get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)
    ):
    return blog.modify(id, request, db)


@router.get("",
         response_model=List[schemas.BlogOut])
def get_blogs(
        db: Session = Depends(database.get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)
    ):
    return blog.get_all(db)


@router.get("/{id}",
         status_code=status.HTTP_200_OK,
         response_model=schemas.BlogOut)
def get_blog_by_id(
        id:int,
        db: Session = Depends(database.get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)
    ):
    return blog.get_one(id, db)

