import os.path

from common_util.file_util import get_ancestor_dir
from model.env import APP_ENV


def get_project_base() -> str:
    if os.path.exists(APP_ENV.PROJECT_BASE):
        return APP_ENV.PROJECT_BASE
    return get_ancestor_dir(__file__, 3)


def app_conf_dir() -> str:
    return os.path.join(get_project_base(), APP_ENV.APP_CONF_DIR)


def app_log_dir() -> str:
    return os.path.join(get_project_base(), APP_ENV.APP_LOG_DIR)


def app_data_dir() -> str:
    return os.path.join(get_project_base(), APP_ENV.APP_DATA_DIR)
