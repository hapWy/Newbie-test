from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import SessionLocal
from app.crud.crud_user import get_user_by_token
from app.db.base import User

ouat2_scheme = OAuth2PasswordBearer(tokenUrl='login')

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
    
async def get_current_user(
        db: AsyncSession = Depends(get_db), token:str = Depends(ouat2_scheme)
) -> User:
    user = await get_user_by_token(db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate":"Bearer"}
        )
    return user



DBSession = Annotated[AsyncSession, Depends(get_db)]
CurrentUser = Annotated[User, Depends(get_current_user)]