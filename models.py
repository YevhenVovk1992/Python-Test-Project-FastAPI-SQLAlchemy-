from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True, unique=True)
    age = Column(Integer, nullable=True)
    email = Column(String, nullable=True, unique=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if 'age' in kwargs:
            if not User._check_age(kwargs['age']):
                raise NotImplemented('Age must be in the range (0, 100]')
            self.age = kwargs['age']

    @classmethod
    def _check_age(cls, num: int):
        if 0 < num <= 100:
            return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email
        }


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True, unique=True)

    def to_dict(self):
        return {
            "name": self.name
        }

class GameSessions(Base):
    __tablename__ = 'game_sessions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_game = Column(Integer, ForeignKey('game.id', ondelete='RESTRICT'), nullable=True)
    id_user = Column(Integer, ForeignKey('user.id', ondelete='RESTRICT'), nullable=True)
    status = Column(String, nullable=True)

    game = relationship('Game', backref='GameSessions')
    user = relationship('User', backref='GameSessions')