from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database import get_db
from ..models import User
import uuid

router = APIRouter(prefix="/api", tags=["Auth"])

class RegisterRequest(BaseModel):
    email: str
    password: str

class RegisterResponse(BaseModel):
    message: str
    user_id: str

@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register_user(request: RegisterRequest, database: Session = Depends(get_db)):
    if not request.email or not request.password:
         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid input")
         
    existing_user = database.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")

    new_user = User(
        user_id=f"user-{uuid.uuid4().hex[:12]}",
        email=request.email,
        password=request.password 
    )
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    
    return {"message": "Account created successfully", "user_id": new_user.user_id}
