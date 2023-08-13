from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, UUID4, constr, validator

class UserBase(BaseModel):
    email: EmailStr
    name: str

class TokenBase(BaseModel):

    token: UUID4 = Field(..., alias='access_token')
    expires: datetime 
    token_tyoe: Optional[str] = 'bearer'

    class Config:
        orm_mode = True
        allow_population_by_field_name=True

    @validator('token')
    def hexify_token(cls, value):
        return value.hex

class UserCreate(UserBase):
    password: constr(strip_whitespace=True, min_length=6)


class Login(BaseModel):
    email: EmailStr
    password: constr(strip_whitespace=True, min_length=6)

class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class User(UserInDBBase):
    token: TokenBase | None = None

