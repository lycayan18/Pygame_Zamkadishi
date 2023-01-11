import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db.requests import add_user, add_game, games_data


def make_session():
    engine = create_engine('sqlite:///db/snake.db')
    new_session = Session(bind=engine)

    return new_session
