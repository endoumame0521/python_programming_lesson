"""
memcachedについて
・データを一時的にメモリ上に保存する
・短い時間の間に何回もデータベースとやり取りをするような処理がある場合に適用する
・そうする事で、データベースからではなくmemcached上からデータを読み込む事で処理速度が早くなる
・あとはデータベースへの短期集中的な不可を減らす事ができる
・データベースの中身の個数カウントとかに使用するのが良い気がする
"""

import sqlite3
# import time

import memcache

# メムキャッシュへ接続する
db = memcache.Client(['127.0.0.1:11211'])

# メムキャッシュにデータをセットする（キーバリュー形式。timeはキャッシュが保存される時間を指定している）
# db.set('web_page', 'value1', time=3)
# time.sleep(1)
# print(db.get('web_page'))

# db.set('counter', 0)
# db.incr('counter', 1)
# db.incr('counter', 1)
# db.incr('counter', 1)
# print(db.get('counter'))

# sqliteでDBにデータを適当に保存する
conn = sqlite3.connect('test_sqlite2.db')
curs = conn.cursor()
# curs.execute('CREATE TABLE persons('
#              'employ_id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
# curs.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()
# conn.close()


# 社員名を渡したら、それに紐づいた社員IDを返してくれる関数を定義
def get_employ_id(name):
    # memcachedから社員名に紐づいた社員IDを取得
    employ_id = db.get(name)
    # 上記がもし見つかれば、その社員IDを返してこの関数を抜ける
    if employ_id:
        return employ_id
    # 見つからなければsqliteのDBからさがす
    curs.execute(
        'SELECT * FROM persons WHERE name = "{}"'.format(name)
    )
    # sqliteのDBから取得したデータをfetchしてpersonという変数に格納する
    person = curs.fetchone()
    # sqliteのDBからも見つからなければ例外処理としてエラーにする
    if not person:
        raise Exception('No employ')
    # DBから取得したデータをアンパッキング（タプル型データをそれぞれ変数に入れる）する
    employ_id, name = person
    # そしてそのデータをmemcachedに60秒間だけ格納する
    db.set(name, employ_id, time=60)
    # 社員IDを返して関数を抜ける
    return employ_id


# Mikeという社員名を渡して社員IDを取得する
print(get_employ_id('Mike'))
