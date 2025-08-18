import sys
import logging
from pathlib import Path
from typing import Optional, Union, Dict
from logging.handlers import TimedRotatingFileHandler


class LogUtil:
    LEVEL_MAP = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self):
        self._loggers: Dict[str, logging.Logger] = {}

    def get_logger(
            self,
            name: str = 'app',
            level: str = 'info',
            log_dir: Optional[Union[str, Path]] = None,
            fmt: str = '[%(levelname)s][%(asctime)s][%(process)s] - [%(module)s.%(funcName)s line:%(lineno)d]: %(message)s',
            rotation: str = 'midnight',
            backup_count: int = 7,
    ) -> logging.Logger:
        if name in self._loggers:
            return self._loggers[name]
        logger = logging.getLogger(name)
        logger.setLevel(self.LEVEL_MAP.get(level.lower(), logging.INFO))
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

        if log_dir:
            log_dir = Path(log_dir)
            log_dir.mkdir(parents=True, exist_ok=True)
            log_file = log_dir / f"{name}.log"
            file_handler = TimedRotatingFileHandler(
                filename=str(log_file),
                when=rotation,
                backupCount=backup_count,
                encoding='utf-8'
            )
            file_handler.setFormatter(logging.Formatter(fmt))
            logger.addHandler(file_handler)
        else:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(logging.Formatter(fmt))
            logger.addHandler(console_handler)

        self._loggers[name] = logger
        return logger

    @staticmethod
    def shutdown():
        logging.shutdown()


# 使用示例
if __name__ == '__main__':
    log_util = LogUtil()

    app_logger = log_util.get_logger(
        name='app',
        level='debug',
        log_dir='./logs',
        rotation='D',  # 每天轮转
        backup_count=30
    )
    db_logger = log_util.get_logger(
        name='database',
        level='info',
        log_dir='./logs',
        fmt='%(asctime)s - %(levelname)s @ %(module)s: %(message)s'
    )

    app_logger.debug("调试信息")
    app_logger.info("服务启动")
    db_logger.warning("数据库连接超时")
    LogUtil.shutdown()
