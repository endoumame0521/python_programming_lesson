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
# logging.basicConfig(filename='test.log', level=logging.INFO)
# formatter = '%(levelname)s:%(message)s'

# フォーマットを指定する事で、ログの表示内容を色々と変更する事ができる
formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# logging.info('info {}'.format('test'))
logging.info('info %s %s', 'test', 'test2')
