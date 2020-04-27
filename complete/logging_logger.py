"""
表題: ロギング

- Pythonにおけるログレベルのオーダー
1 CRITICAL
2 ERROR
3 WARNING <---WANING、これより下(INFO, DEBUG)は表示されない
4 INFO
5 DEBUG
"""


import logging

# サブモジュールをインポート
import logtest

# loggingは通常メイン関数のファイルに記述する
logging.basicConfig(level=logging.INFO)

logging.info('info')

# loggingを記述した後はloggerを使ってカスタマイズしていく
logger = logging.getLogger(__name__)
logger.info('from main')

logtest.do_something()

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.debug('debug')
