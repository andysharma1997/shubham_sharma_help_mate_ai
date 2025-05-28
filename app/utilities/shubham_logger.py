from logging import getLogger, INFO, Formatter, LoggerAdapter, StreamHandler
# from logging.handlers import TimedRotatingFileHandler
from app.middlewares.contextmiddleware import ContextMiddelware
import sys

def get_logger(name, level=INFO):
    """logger method to get logger from
    author: andy
    Args:
        name (_type_): _description_
    Returns:
        _type_: _description_
    """

    handler = StreamHandler(sys.stdout)
    log_format = " %(levelname)s : %(asctime)-5s %(filename)s:%(lineno)d %(funcName)-5s --> %(message)s"
    formatter = Formatter(log_format)
    handler.setFormatter(formatter)
    logger = getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger





class ShubhamLogger(LoggerAdapter):
    """Base class with logger enabled with adding a uniqueid for each request
    author: andy
    Args:
        logging ([type]): [description]
    """
    def process(self, msg, kwargs):
        if ContextMiddelware.get_request_id() is not None:

            return '[request_id: %s]' % (ContextMiddelware.get_request_id()), kwargs
        else:
            return '%s' % (msg), kwargs