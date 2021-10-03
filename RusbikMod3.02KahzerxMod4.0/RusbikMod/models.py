from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Numeric, CHAR, ForeignKey
from sqlalchemy.orm import relationship, backref


class Database:
    _base = declarative_base()

    class PlayerTable(_base):
        __tablename__ = "player"

        name = Column(String(20), primary_key=True, nullable=False)
        discordId = Column(Numeric, default=None)
        timesJoined = Column(Numeric, default=0)
        isBanned = Column(Numeric, default=0)
        perms = Column(Numeric, default=1)

        def __init__(self, name, discordID, timesJoined, isBanned, perms):
            self.name = name
            self.discordId = discordID
            self.timesJoined = timesJoined
            self.isBanned = isBanned
            self.perms = perms

    class PosTable(_base):
        __tablename__ = "pos"

        name = Column(String(20), ForeignKey("player.name"), primary_key=True, nullable=False)

        deathX = Column(Numeric, default=None)
        deathY = Column(Numeric, default=None)
        deathZ = Column(Numeric, default=None)
        deathDim = Column(CHAR(20), default=None)

        homeX = Column(Numeric, default=None)
        homeY = Column(Numeric, default=None)
        homeZ = Column(Numeric, default=None)
        homeDim = Column(CHAR(20), default=None)

        id = relationship("PlayerTable", backref=backref("pos", uselist=False))

        def __init__(self, name, deathX, deathY, deathZ, deathDim, homeX, homeY, homeZ, homeDim):
            self.name = name
            self.deathX = deathX
            self.deathY = deathY
            self.deathZ = deathZ
            self.deathDim = deathDim
            self.homeX = homeX
            self.homeY = homeY
            self.homeZ = homeZ
            self.homeDim = homeDim

    def __init__(self, file_path: str):
        self._engine = create_engine("sqlite:///" + file_path, echo=False)
        self._base.metadata.create_all(self._engine)

    def get_engine(self):
        return self._engine
