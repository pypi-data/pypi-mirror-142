from peewee import SqliteDatabase
from .model import Note, database_proxy

# TODO(andre): add support for other DB types
def _sqlite_db(cfg):
    db_path = cfg['path']
    return SqliteDatabase(db_path)

TYPE_MAPPING = dict(sqlite=_sqlite_db)

class DatabaseLoader:
    def __init__(self, cfg):
        self._cfg = cfg

    def load(self):
        db_type = self._cfg['type']
        if db_type not in TYPE_MAPPING:
            raise Exception(f'db type {db_type} not supported. currently supported {TYPE_MAPPING.keys()}')
        database = TYPE_MAPPING[db_type](self._cfg)
        database_proxy.initialize(database)
        database.connect()
        database.create_tables([
            Note
        ])
        return database
