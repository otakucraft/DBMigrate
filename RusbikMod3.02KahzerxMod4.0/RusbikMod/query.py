from sqlalchemy import MetaData, Table, select
from sqlalchemy.orm import sessionmaker


class Query:
    def __init__(self, db: Database):
        self.db = db
        self.session = sessionmaker(bind=db.get_engine())()
        self.metadata = MetaData(bind=None)

    def get_player_data(self):
        table = Table(
            self.db.PlayerTable.__tablename__, self.metadata, autoload=True, autoload_with=self.db.get_engine()
        )
        res = self.session.execute(select(table)).fetchall()
        print(res)
