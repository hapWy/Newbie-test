from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import relationship


from app.db.base_class import Base


class Title(Base):
    __tablename__='title'

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(ForeignKey('user_teams.id'))
    added_to = Column(DateTime())
    title = Column(String(100), unique=True)
    chapters = Column(Text)




