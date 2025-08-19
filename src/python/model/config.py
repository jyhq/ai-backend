import multiprocessing
from common_util import file_util


class Server:
    def __init__(self, host: str, port: int, api_version: str):
        self.host = host
        self.port = port
        self.api_version = api_version

class Database:
    def __init__(self, host: str, port: int, name: str, user: str, password: str):
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password

class Gunicorn:
    def __init__(self, workers: int, timeout: int):
        if workers < 0:
            workers = multiprocessing.cpu_count()
        self.workers = workers
        self.timeout = timeout


class Config:
    def __init__(self, server: Server, database: Database, gunicorn: Gunicorn):
        self.server = server
        self.database = database
        self.gunicorn = gunicorn


def get_config_object(conf_path) -> Config:
    config = file_util.load_yaml_conf(conf_path)
    server = Server(**config.get("server", {}))
    database = Database(**config.get("database", {}))
    gunicorn = Gunicorn(**config.get("gunicorn", {}))
    return Config(
        server=server,
        database=database,
        gunicorn=gunicorn,
    )
