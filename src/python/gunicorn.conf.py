from util import app_util, dir_util

# from env or config
proc_name = app_util.APP_ENV.APP_NAME
bind = f"{app_util.app_config().server.host}:{app_util.app_config().server.port}"
loglevel = app_util.APP_ENV.LOG_LEVEL
pidfile = f"{dir_util.get_project_base()}/gun.pid"
workers = app_util.app_config().gunicorn.workers
timeout = app_util.app_config().gunicorn.timeout

# no need to modify
preload_app = True
worker_class = "uvicorn.workers.UvicornWorker"
