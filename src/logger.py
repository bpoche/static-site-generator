import os
import logging
from logging.config import dictConfig
from datetime import datetime

def setup_logging():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Move up one directory from the script directory
    parent_dir = os.path.dirname(script_dir)
    
    # Construct the path to the log files
    log_file_path = os.path.join(parent_dir, 'static-site-gen-v2.log')
    current_log_file_path = os.path.join(parent_dir, 'static-site-gen-v2-current.log')

    logging_config = {
        'version': 1,
        'formatters': {
            'json': {
                # 'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
                'format':'{"time": "%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "module": "%(module)s", "func": "%(funcName)s", "line": "%(lineno)d", "message": "%(message)s"}',
            },
            'aligned': {
                'format': (
                    '%(asctime)s %(levelname)-6s '
                    'mod:%(module)-15s %(lineno)s:%(funcName)-20s %(message)s'
                )
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'aligned',
                'level': logging.DEBUG
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'json',
                'level': logging.INFO,
                'filename': log_file_path,
                'maxBytes': 500 * 1024,  # 500 KB
                'backupCount': 2
            },
            'current_file': {
                'class': 'logging.FileHandler',
                'formatter': 'json',
                'level': logging.INFO,
                'filename': current_log_file_path,
                'mode': 'w+'
            },
        },
        'root': {
            'handlers': ['console', 'file', 'current_file'],
            'level': logging.INFO,
        },
    }
    dictConfig(logging_config)

# Setup logging according to the above configuration
setup_logging()
# Create and export the logger for use in other modules
logger = logging.getLogger(__name__)

'''
%(name)s
    Description: The name of the logger that handled the log message.
    Example: root, my_module

%(levelname)s
    Description: The text representation of the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
    Example: INFO, ERROR

%(asctime)s
    Description: The time when the LogRecord was created.
    Example: 2024-07-22 12:00:00

%(message)s
    Description: The log message output by the user, which is constructed using the msg and args provided to the logging call.
    Example: Starting process...

%(pathname)s
    Description: The full path of the source file where the logging call was made.
    Example: /path/to/my_module.py

%(filename)s
    Description: The filename portion of the pathname.
    Example: my_module.py

%(module)s
    Description: The module name where the logging call was made (derived from filename).
    Example: my_module

%(lineno)d
    Description: The line number in the source file where the logging call was made.
    Example: 42

%(funcName)s
    Description: The name of the function or method from which the logging call was made.
    Example: start_process

%(threadName)s
    Description: The name of the thread in which the logging call was made.
    Example: MainThread

%(thread)d
    Description: The numeric ID of the thread in which the logging call was made.
    Example: 139931098269696

%(process)d
    Description: The process ID (PID) of the process in which the logging call was made.
    Example: 12345

%(processName)s
    Description: The name of the process in which the logging call was made.
    Example: MainProcess

%(created)f
    Description: The time in seconds since the epoch as a floating-point number when the LogRecord was created.
    Example: 1626983243.376

%(relativeCreated)d
    Description: The time in milliseconds since the Logger was created when the LogRecord was created.
    Example: 12345

%(msecs)d
    Description: The millisecond portion of the asctime.
    Example: 123

%(levelno)d
    Description: The numeric logging level for the message (e.g., 10 for DEBUG, 20 for INFO).
    Example: 20

%(exc_info)s
    Description: The exception information formatted as a string. This is typically None unless an exception occurred.
    Example: None, Traceback (most recent call last): ...

%(stack_info)s
    Description: Stack information formatted as a string.
    Example: Stack (most recent call last): ...
'''