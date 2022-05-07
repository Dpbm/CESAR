import logging
from os import path

logger_log_file = 'logs.log'

if(not path.exists(logger_log_file)):
    open(logger_log_file, 'w').close()


logger = logging.getLogger(__name__)

logging.basicConfig(
    filename=logger_log_file,
    level=logging.DEBUG,
    format='%(asctime)s:%(name)s:%(message)s'
)
