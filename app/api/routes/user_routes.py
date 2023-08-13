from fastapi import APIRouter, HTTPException

from app.api.deps import CurrentUser, DBSession
from app.crud import crud_user
from app.schemas.user import Login, User, UserCreate

router = APIRouter()

@router.post('/sing-up', response_model=User)
async def create_user(user: UserCreate, db: DBSession):
    user_db = await crud_user.get_user_by_email(db, email=user.email)
    if user_db:
        raise HTTPException(status_code=400, detail='User already registered')
    user = await crud_user.create_user(db, user=user)
    user.token = await crud_user.create_token(db, user=user)
    return user


@router.post('/login/', response_model=User)
async def login(user: Login, db:DBSession):
    user_db = await crud_user.get_user_by_email(db, email=user.email)
    if not user_db:
        raise HTTPException(status_code=400, detail="User not found")
    if user_db.password != user.password:
        raise HTTPException(status_code=400, detail='User not found')
    return user_db