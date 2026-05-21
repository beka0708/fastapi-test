from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserResponse
import crud.user as crud


router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/', response_model=list[UserResponse])
def get_users():
    return crud.get_all_users()


@router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int):
    user = crud.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='Пользователь не найден')
    return user


@router.post('/', response_model=UserResponse, status_code=201)
def create_user(data: UserCreate):
    return crud.create_user(data.name, data.email)
