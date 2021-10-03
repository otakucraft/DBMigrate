from sqlalchemy import MetaData, Table, select
from sqlalchemy.orm import sessionmaker

from KahzerxMod.models import Database


class Query:
    def __init__(self, db: Database):
        self.db = db
        self.session = sessionmaker(bind=db.get_engine())()
        self.metadata = MetaData(bind=None)
