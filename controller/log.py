import logging
log_format = "\33[37m[ %(levelname)s ] %(asctime)s :: %(name)s :: %(module)s :: %(message)s\33[1m"
logging.basicConfig(format=log_format, level=logging.INFO, filemode='w')


def degub(message):
    logging.debug(f"\33[36m{message}\33[0m")


def info(message):
    logging.info(f"\33[32m{message}\33[0m")


def error(message):
    logging.error(f"\33[31m{message}\33[0m")