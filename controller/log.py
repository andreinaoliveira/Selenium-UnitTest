import logging
log_format = '%(asctime)s :: %(name)s :: %(levelname)s :: %(module)s :: %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO, filemode='w')


def degub(message):
    logging.debug(message)

def info(message):
    logging.info(message)

def error(message):
    logging.error(message)
