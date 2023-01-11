from db.models import Users, Games
from sqlalchemy.orm import Session
from sqlalchemy import subquery
from sqlalchemy.sql import func


def add_user(session, name):  # добавить игрока
    c = Users(
        Username=name
    )

    session.add(c)
    session.commit()


def add_game(session, name, score=0, time=0):  # добавит результаты игры по имени игрока
    c = Games(
        UserId=session.query(Users.UserId).filter(Users.Username == name).all()[0][0],
        Score=score,
        Time=time
    )

    session.add(c)
    session.commit()


def games_data(session):  # топ рекордов
    q = session.query(Users.Username, Games.Score).join(Games).order_by(-Games.Score).group_by(Users.UserId).all()

    return q
