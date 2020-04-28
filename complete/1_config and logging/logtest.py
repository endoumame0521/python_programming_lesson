import logging


# loggingを記述した後はloggerを使ってカスタマイズしていく
logger = logging.getLogger(__name__)
# これはloggerを使ってloggingで設定したログレベル(INFO)を(DEBUG)に変更している
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('logtest.log')
logger.addHandler(h)

def do_something():
    logger.info('from logtest')
    logger.debug('from logtest debug')
