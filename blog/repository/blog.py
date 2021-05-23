from sqlalchemy.orm import Session
from blog import schemas, models
from fastapi import status, HTTPException


def create(request: schemas.Blog, db: Session, user: models.User):
    new_blog = models.Blog(
            title=request.title,
            body=request.body,
            user_id=user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()

    return {"message": "delete success!"}


def modify(id: int, request: models.Blog, db: Session):
    obj = {
        "title": request.title,
        "body": request.body,
    }
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update(obj,synchronize_session=False)
    db.commit()

    return {"message": "updated success!"}


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_one(id: int, db: Session):
    blog_item = db.query(models.Blog).filter(models.Blog.id==id).first()

    if not blog_item:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with the id {id} is not available"
            )

    return blog_item

