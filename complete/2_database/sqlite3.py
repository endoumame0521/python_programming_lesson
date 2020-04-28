# SQLite

import sqlite3

# 実際にtest_sqlite.dbを作成する
# conn = sqlite3.connect('test_sqlite.db')

# メモリ上に一時的にデータベースを作成する。よって何回createしてもエラーにならない。
conn = sqlite3.connect(':memory:')

# カーソルを作成
curs = conn.cursor()

# personsテーブルを作成するSQL文を実行
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
conn.commit() # データベースに内容を反映させる

# personsテーブルのnameカラムに"Mike"を挿入するSQL文を実行
curs.execute(
    'INSERT INTO persons(name) values("Mike")')
conn.commit()

# personsテーブルのnameカラムに"Nancy"を挿入するSQL文を実行
curs.execute(
    'INSERT INTO persons(name) values("Nancy")')
conn.commit()

# personsテーブルのnameカラムに"Jun"を挿入するSQL文を実行
curs.execute(
    'INSERT INTO persons(name) values("Jun")')
conn.commit()

# personsテーブルのnameカラム"Mike"を"Michel"に更新するSQL文を実行
curs.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
conn.commit()

# personsテーブルのnameカラム"Michel"を削除するSQL文を実行
curs.execute('DELETE FROM persons WHERE name = "Michel"')
conn.commit()

# personsテーブルの内容を確認するSQL文を実行
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

# カーソル を閉じる
curs.close()
# コネクションを閉じる
conn.close()
