from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas import UserCreate, UserLogin
from app.dependencies.database import get_db
from app.models.user import User
from app.core import hash_password, verify_password, create_access_token
router = APIRouter()

@router.post("/register", tags=["register"])
def register(user:UserCreate, db:Session = Depends(get_db)):

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()

    return {
       "message": "User created successfully",
    }


@router.post("/login", tags=["login"])
def login(user:UserLogin, db:Session = Depends(get_db)):

   stmt = select(User).where(User.email == user.email)
   existing_user = db.scalar(stmt)

   if existing_user is None:
       raise HTTPException(status_code=401, detail="User not found")

   if not verify_password(user.password, existing_user.password):
       raise HTTPException(status_code=401, detail="Incorrect password")

   access_token = create_access_token({"sub":str(existing_user.id)})

   return {
       "access_token": access_token,
       "token_type": "bearer",
   }

