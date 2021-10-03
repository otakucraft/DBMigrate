from sqlalchemy import MetaData, Table, select
from sqlalchemy.orm import sessionmaker

from RusbikMod.models import Database


class Query:
    def __init__(self, db: Database):
        self.db = db
        self.session = sessionmaker(bind=db.get_engine())()
        self.metadata = MetaData(bind=None)

    def get_player_data(self) -> list[Database.PlayerTable]:
        table = Table(
            self.db.PlayerTable.__tablename__, self.metadata, autoload=True, autoload_with=self.db.get_engine()
        )
        res: list[Database.PlayerTable] = self.session.execute(select(table)).fetchall()
        return res

    def get_player_pos_data(self, player_name) -> Database.PosTable:
        table = Table(
            self.db.PosTable.__tablename__, self.metadata, autoload=True, autoload_with=self.db.get_engine()
        )
        res: Database.PosTable = self.session.execute(select(table).where(table.columns.name == player_name)).fetchone()
        return res
