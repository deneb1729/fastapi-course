from fastapi import Depends, status, HTTPException
from blog.token import verify_token
from fastapi.security import OAuth2PasswordBearer
from blog.repository.user import get_by_email
from sqlalchemy.orm import Session
from blog.database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})

    token_data = verify_token(token, credentials_exception)
    user = get_by_email(token_data.email, db)
    if user is None:
        raise credentials_exception

    return user

