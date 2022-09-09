import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, User, Game, GameSessions

app = FastAPI()
connect_to_db = "sqlite:///test"
engine = create_engine(connect_to_db, echo=True, future=True)
session = Session(engine)


@app.get("/api/v1.0/get_games")
async def get_games() -> list:
    """
    Get list of all games and users who connected to them games
    :return: list of the game
    """
    json_data = []
    games_lst = session.query(
        Game.name, User.name, GameSessions.status
    ).join(Game, GameSessions.id_game == Game.id).join(User, GameSessions.id_game == User.id).all()
    for el in games_lst:
        game = {'game': el[0], 'user': el[1], 'status': el[2]}
        json_data.append(game)
    return json_data


@app.get("/api/v1.0/get_me")
async def get_me(user_id: int) -> list:
    """
    Get info about current user and info about all connected games
    :param user_id: current user
    :return: user info
    """
    json_data = []
    current_user_info = session.query(
        User.name, User.age, User.email, Game.name, GameSessions.status
    ).join(GameSessions, User.id == GameSessions.id_user).join(
        Game, Game.id == GameSessions.id_game
    ).filter(User.id == user_id).all()
    for el in current_user_info:
        game = {'user name': el[0], 'age': el[1], 'email': el[2], 'play game': el[3], 'game status': el[4]}
        json_data.append(game)
    return json_data


@app.post("/api/v1.0/connect_to_game")
async def connect_to_game(id_game, id_user):
    """
    When user send this request. Need to create one obj like User - Game
    :param id_game: starting game
    :return: status code
    """
    play_game = GameSessions(id_game=id_game, id_user=id_user, status='online')
    try:
        session.add(play_game)
        session.commit()
    except:
        return {"status": "ERROR"}
    return {"status": "SUCCESS"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
