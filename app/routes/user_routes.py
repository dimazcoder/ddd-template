from fastapi import APIRouter, Depends, HTTPException
from app.services.user_service import UserService
from .schemas.user_schemas import UserResponse
from app.deps.user_deps import get_user_service

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(username: str, email: str, hashed_password: str, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(username, email, hashed_password)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user_by_id(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    try:
        user = user_service.get_user_by_id(user_id)
        if user:
            return user
        raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")