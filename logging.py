import logging

logging.basicConfig(filename="dhruv.log",
                    level=logging.DEBUG,
                    format="{asctime}:{lineno}: {process}: {message}: {levelname}: {name}",
                    datefmt='%d-%b-%y %M:%H:%S', style="{")

logging.debug("this is debug message")
logging.info('The info message is displaying')
logging.warning('The warning message is displaying')
logging.error('The error message is displaying')
logging.critical('The critical message is displaying')
