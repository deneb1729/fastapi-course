from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import database, schemas, models
from blog.repository import user


router = APIRouter(prefix="/user",tags=["Users"])


@router.post("",
          status_code=status.HTTP_201_CREATED,
          response_model=schemas.UserOut)
def create_user(
        request: schemas.User,
        db: Session = Depends(database.get_db)
    ):
    return user.create(request, db)


@router.get("/{id}",
         status_code=status.HTTP_200_OK,
         response_model=schemas.UserOut)
def get_user_by_id(id:int, db: Session = Depends(database.get_db)):
    return user.get_one(id, db)

