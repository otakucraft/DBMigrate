from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, CHAR


class Database:
    _base = declarative_base()

    class PlayerTable(_base):
        __tablename__ = "player"

        name = Column(String(20), primary_key=True, nullable=False)
        discordId = Column(Integer, default=None)
        timesJoined = Column(Integer, default=0)
        isBanned = Column(Integer, default=0)
        perms = Column(Integer, default=1)

    class PosTable(_base):
        __tablename__ = "pos"

        name = Column(String(20), primary_key=True, nullable=False)
        deathX = Column(Integer, default=None)
        deathY = Column(Integer, default=None)
        deathZ = Column(Integer, default=None)
        deathDim = Column(CHAR(20), default=None)

        homeX = Column(Integer, default=None)
        homeY = Column(Integer, default=None)
        homeZ = Column(Integer, default=None)
        homeDim = Column(CHAR(20), default=None)

    def __init__(self, file_path: str):
        self._engine = create_engine(file_path, echo=False)
        self._base.metadata.create_all(self._engine)

    def get_engine(self):
        return self._engine
