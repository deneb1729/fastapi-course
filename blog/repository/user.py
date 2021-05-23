from sqlalchemy.orm import Session
from blog import schemas, models
from blog.utils import Hash
from fastapi import status, HTTPException


def create(request: schemas.User, db: Session):
    password = Hash.bcrypt(request.password)
    new_user = models.User(
            name=request.name,
            email=request.email,
            password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_one(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} not found")
    
    return user


def get_by_email(email: str, db: Session):
    return db.query(models.User).filter(models.User.email == email).first()

