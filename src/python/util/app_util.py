import os

from common_util import log
from model.config import get_config_object
from model.const import CONF_FMT
from model.env import APP_ENV
from util.dir_util import app_conf_dir, app_log_dir


def app_config():
    return get_config_object(os.path.join(app_conf_dir(), CONF_FMT.format(APP_ENV.APP_ENV)))


def app_logger():
    return log.LogUtil().get_logger(name=APP_ENV.APP_NAME, level=APP_ENV.LOG_LEVEL, log_dir=app_log_dir())
