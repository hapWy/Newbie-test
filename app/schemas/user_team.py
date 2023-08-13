from typing import Optional

from pydantic import BaseModel

class UserTeamBase(BaseModel):
    name: str

class UserTeamInDBBase(UserTeamBase):
    id: Optional[int] = None
