from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import User, UserTeam, UserTeamAssociation
from app.schemas.user_team import UserTeamBase

async def create_team(
        db: AsyncSession, user: User, team: UserTeamBase
)  -> UserTeam:
    db_user_team = UserTeam(
        name=team.name
    )
    db_user_team.users.append(user)
    db.add(db_user_team)
    await db.commit()
    await db.refresh(db_user_team)
    return db_user_team
