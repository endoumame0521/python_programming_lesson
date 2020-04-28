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
# import logtest

# loggingは通常メイン関数のファイルに記述する
logging.basicConfig(level=logging.INFO)


# ログに掛けるフィルターの内容を定義（logging.Filterクラスを継承)
class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


# loggingを記述した後はloggerを使ってカスタマイズしていく
logger = logging.getLogger(__name__)
# loggerに上記で定義したフィルターを追加
# これによりログの出力文字の中に'password'という文字列が含まれている場合はログが出力されなくなる
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('from main password = "test"')

# logtest.do_something()
