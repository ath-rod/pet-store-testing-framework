import logging.config
import os
import sys

API_BASE_URI = "https://petstore.swagger.io/v2"
UI_BASE_URI = "https://petstore.octoperf.com/actions"

project_root = os.path.dirname(__file__)
logger_dir = os.path.join(project_root, "Logs")
if not os.path.exists(logger_dir):
    os.makedirs(logger_dir)

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'cli_format': {'format': '%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)s) %(message)s',
                       'datefmt': "%H:%M:%S"},
        'file_format': {'format': '%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)s) %(message)s',
                        'datefmt': "%Y-%m-%d %H:%M:%S"}
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'cli_format',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'file_format',
            'filename': f"{logger_dir}\\pet_store.log",
            'maxBytes': 1048576,
            'backupCount': 3
        }
    },
    'loggers': {
        'default': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})

logger = logging.getLogger('default')


# Catches all UNCAUGHT exceptions to log - see https://stackoverflow.com/a/16993115
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception
