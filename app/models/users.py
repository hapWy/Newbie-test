import uuid

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, force_auto_coercion, PasswordType

from app.db.base_class import Base


force_auto_coercion()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(20), unique = True)
    name = Column(String(30))
    email = Column(EmailType(50), index=True, nullable=False)
    password = Column(PasswordType(schemes=["pbkdf2_sha512"]), nullable=False)

class UserKeys(Base):
    __tablename__='user_keys'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    public_key = Column(String(2000), nullable=False)
    is_revoked=Column(Boolean, default=False)

    user = relationship('User',back_populates='keys')



class UserToken(Base):
    __tablename__='user_tokens'

    id = Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    token = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    
    expires=Column(DateTime)

    user = relationship('User', back_populates='tokens', lazy='joined')

class UsersTeam(Base):
    __tablename__='user_teams'

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(50), unique=True)
    users = relationship('User', secondary='user_group_association', back_populates='teams')
    titles = relationship('Product', back_populates='user_team', cascade="all, delete-orphan")



class UserTeamAssociation(Base):
    __tablename__='user_team_association'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    team_id=Column(ForeignKey('user_teams.id'))

