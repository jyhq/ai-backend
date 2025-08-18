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


class Config:
    def __init__(self, server: Server, database: Database):
        self.server = server
        self.database = database


def get_config_object(conf_path) -> Config:
    config = file_util.load_yaml_conf(conf_path)
    server = Server(**config.get("server", {}))
    database = Database(**config.get("database", {}))
    return Config(
        server=server,
        database=database,
    )
