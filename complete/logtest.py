import logging

# loggingを記述した後はloggerを使ってカスタマイズしていく
logger = logging.getLogger(__name__)
# これはloggerを使ってloggingで設定したログレベル(INFO)を(DEBUG)に変更している
logger.setLevel(logging.DEBUG)

def do_something():
    logger.info('from logtest')
    logger.debug('from logtest debug')
