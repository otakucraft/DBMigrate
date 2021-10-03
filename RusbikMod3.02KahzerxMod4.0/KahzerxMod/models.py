from sqlalchemy import create_engine, Column, VARCHAR, ForeignKey, NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


class Database:
    _base = declarative_base()

    class PlayerTable(_base):
        __tablename__ = "player"

        uuid = Column(VARCHAR(50), primary_key=True, nullable=False)
        name = Column(VARCHAR(50), default=None)

        def __init__(self, uuid, name):
            self.uuid = uuid
            self.name = name

    class BackTable(_base):
        __tablename__ = "back"

        uuid = Column(VARCHAR(50), ForeignKey("player.uuid"), primary_key=True, nullable=False)
        deathX = Column(NUMERIC, default=None)
        deathY = Column(NUMERIC, default=None)
        deathZ = Column(NUMERIC, default=None)
        deathDim = Column(NUMERIC, default=None)

        id = relationship("PlayerTable", backref=backref("back", uselist=False))

        def __init__(self, uuid, deathX, deathY, deathZ, deathDim):
            self.uuid = uuid
            self.deathX = deathX
            self.deathY = deathY
            self.deathZ = deathZ
            self.deathDim = deathDim

    class HomeTable(_base):
        __tablename__ = "home"

        uuid = Column(VARCHAR(50), ForeignKey("player.uuid"), primary_key=True, nullable=False)
        homeX = Column(NUMERIC, default=None)
        homeY = Column(NUMERIC, default=None)
        homeZ = Column(NUMERIC, default=None)
        homeDim = Column(NUMERIC, default=None)

        id = relationship("PlayerTable", backref=backref("home", uselist=False))

        def __init__(self, uuid, homeX, homeY, homeZ, homeDim):
            self.uuid = uuid
            self.homeX = homeX
            self.homeY = homeY
            self.homeZ = homeZ
            self.homeDim = homeDim

    class PermsTable(_base):
        __tablename__ = "perms"

        uuid = Column(VARCHAR(50), ForeignKey("player.uuid"), primary_key=True, nullable=False)
        level = Column(NUMERIC, default=1)

        id = relationship("PlayerTable", backref=backref("perms", uselist=False))

        def __init__(self, uuid, level):
            self.uuid = uuid
            self.level = level

    class DiscordTable(_base):
        __tablename__ = "discord"

        uuid = Column(VARCHAR(50), ForeignKey("player.uuid"), primary_key=True, nullable=False)
        discordID = Column(NUMERIC, primary_key=True, nullable=False)

        id = relationship("PlayerTable", backref=backref("discord", uselist=False))

        def __init__(self, uuid, discordID):
            self.uuid = uuid
            self.discordID = discordID

    class DiscordBannedTable(_base):
        __tablename__ = "discord_banned"

        discordID = Column(NUMERIC, ForeignKey("discord.discordID"), primary_key=True, nullable=False)

        id = relationship("DiscordTable", backref=backref("discord_banned", uselist=False))

        def __init__(self, discordID):
            self.discordID = discordID

    def __init__(self, file_path: str):
        self._engine = create_engine("sqlite:///" + file_path, echo=False)
        self._base.metadata.create_all(self._engine)

    def get_engine(self):
        return self._engine
