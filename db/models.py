from sqlalchemy.dialects.sqlite import INTEGER, TEXT, REAL
from sqlalchemy import Column, ForeignKey
from db.base import Base


class Users(Base):
    __tablename__ = 'Users'

    UserId = Column(INTEGER, primary_key=True, autoincrement=True)
    Username = Column(TEXT)


class Games(Base):
    __tablename__ = 'Games'

    GameId = Column(INTEGER, primary_key=True, autoincrement=True)
    UserId = Column(INTEGER,  ForeignKey('Users.UserId'))
    Score = Column(INTEGER)
    Time = Column(REAL)
