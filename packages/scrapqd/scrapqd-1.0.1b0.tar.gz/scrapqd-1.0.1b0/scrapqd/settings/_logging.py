import os
import logging

log_level = os.environ.get('SCRAPQD_LOG_LEVEL', logging.ERROR)

_log_format = "[%(levelname)s] [%(process)d] [%(asctime)s] [SCRAPQD] " \
              "[%(pathname)s:%(funcName)s():%(lineno)s] " \
              "[%(name)s] [%(message)s]"

logging.basicConfig(format=_log_format,
                    datefmt="%Y-%m-%dT%H:%M:%S%z",
                    level=log_level)
