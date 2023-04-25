import logging.config
import os

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
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'cli_format',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'DEBUG',
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
