import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db.requests import add_user, add_game, games_data


def session():
    engine = create_engine('sqlite:///db/snake.db')
    session = Session(bind=engine)

    return session


session = session()
print(games_data(session))
