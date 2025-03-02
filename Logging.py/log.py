import logging
"""logging.basicConfig(format = '%(asctime)s %(levelname)-8s:%(message)s' ,filename='example.log', level=logging.DEBUG)
asctime = human-readable time when the LogRecord was created.
levelname = the textual representation of the log level.
message = the log message.
filename = the file from which the log message originated.

logging.debug('This message should go to the log file')"""
logger = logging.getLogger('my_logger')

logger.info('This is not a warning.')
logger.warning('This is a warning.')
logger.error('This is an error.')
logger.critical('This is a critical error.')
logger.debug('This is a debug message.')
"""
DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
"""
