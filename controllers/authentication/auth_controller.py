from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from configs.database import get_db
from dtos.auth_dtos import UserCreate, User
from services.authentication.auth_service import create_user, authenticate_user, create_access_token, get_current_user

router = APIRouter()

# Authentication endpoints
@router.post("/register", response_model = User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user.dict())
    if db_user is None:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    return db_user


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }


@router.get("/users/me", response_model= User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

