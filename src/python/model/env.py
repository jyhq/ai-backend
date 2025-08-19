from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnv(BaseSettings):
    APP_NAME: str = "app"
    APP_DESC: str = "fastapi server"
    APP_VERSION: str = '0.0.1'
    LOG_LEVEL: Literal['debug', 'info', 'warning', 'error', 'critical'] = 'debug'
    APP_ENV: Literal['dev', 'test', 'pro'] = 'dev'

    PROJECT_BASE: str = ""
    APP_CONF_DIR: str = "conf"
    APP_LOG_DIR: str = "log"
    APP_DATA_DIR: str = "data"
    GUN_PID_FILE: str = "gun.pid"

    model_config = SettingsConfigDict(
        env_file=f".env",
        env_file_encoding='utf-8',
        extra='ignore'
    )


APP_ENV = AppEnv()
