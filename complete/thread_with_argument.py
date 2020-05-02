import logging
import threading
import time


# スレッド名を表示するログを設定
logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')


def worker2(x, y=1):
    logging.debug('start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    logging.debug('end')


if __name__ == '__main__':
    # スレッドを作成
    t1 = threading.Thread(name='rename worker1', target=worker1)
    # スレッドを作成(引数を渡している)
    t2 = threading.Thread(
        target=worker2, args=(100, ), kwargs={'y': 200})
    # スレッドを開始
    t1.start()
    # スレッドを開始
    t2.start()

    logging.debug('start')
    time.sleep(5)
    logging.debug('end')
