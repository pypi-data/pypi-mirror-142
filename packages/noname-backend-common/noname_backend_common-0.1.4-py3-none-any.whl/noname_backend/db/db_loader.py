from peewee import SqliteDatabase

# TODO(andre): add support for other DB types
def _sqlite_db(cfg):
    db_path = cfg['path']
    return SqliteDatabase(db_path)

TYPE_MAPPING = dict(sqlite=_sqlite_db)

class DatabaseLoader:
    def __init__(self, cfg, database_proxy, models):
        self._cfg = cfg
        self._database_proxy = database_proxy
        self._models = models

    def load(self):
        db_type = self._cfg['type']
        if db_type not in TYPE_MAPPING:
            raise Exception(f'db type {db_type} not supported. currently supported {TYPE_MAPPING.keys()}')
        database = TYPE_MAPPING[db_type](self._cfg)
        self._database_proxy.initialize(database)
        database.connect()
        database.create_tables(models)
        return database
