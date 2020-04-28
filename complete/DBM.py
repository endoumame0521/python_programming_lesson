"""
DBM データベースについて
・Pythonの標準ライブラリのDB
・ストリング型の文字列しか保存できない
・なので主にcacheなどを保存するのに使用する
"""

import dbm


with dbm.open('cache', 'c') as db:
    db['key1'] = 'value1'
    db['key2'] = 'value2'

#     これはintegerなのでDBに保存できない
#     db['key3'] = 1

with dbm.open('cache', 'r') as db:
    print(db.get('key1'))
