from typing import Optional

from pydantic import BaseModel


class TitleBase(BaseModel):
    title: str
    chapters: str
    team_id: int

class TitleInDBBase(TitleBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True