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

# ロギングのレベルを変更している
# こうする事で、waning以下も表示する事ができる
logging.basicConfig(filename='test.log', level=logging.INFO)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# logging.info('info {}'.format('test'))
logging.info('info %s %s', 'test', 'test2')
