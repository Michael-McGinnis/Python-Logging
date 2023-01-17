# import logging is root access by default. It is possible to create your own

import logging

logger = logging.getLogger(__name__) #__name__ is a global variable that 
# will use the name of helplog
#logger.info('Greetings!')

# Create handler

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('This is an error')