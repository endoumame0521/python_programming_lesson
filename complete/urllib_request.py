"""
REST

HTTPメソッド　クライアントが行いたい処理をサーバーに伝える

GET     データの参照
POST    データの新規登録
PUT     データの更新
DELETE  データの削除
"""

import urllib.request
import json


# GETでjson形式で取得

# URLにパラメータを付けたい時
# payload = {'key1': 'value1', 'key2': 'value2'}
# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# 出力結果
# url => http://httpbin.org/get?key1=value1&key2=value2

# with urllib.request.urlopen(url) as f:
#     r = json.loads(f.read().decode('utf-8'))


# POSTでjson形式で取得
# payload = json.dumps(payload).encode('utf-8')
# req = urllib.request.Request(
#     'http://httpbin.org/post', data=payload, method='POST')
# with urllib.request.urlopen(req) as f:
#     r = json.loads(f.read().decode('utf-8'))
#     print(r)


# PUTでjson形式で取得
# req = urllib.request.Request(
#     'http://httpbin.org/put', data=payload, method='PUT')
# with urllib.request.urlopen(req) as f:
#     r = json.loads(f.read().decode('utf-8'))
#     print(r)


# DELETEでjson形式で取得
# req = urllib.request.Request(
#     'http://httpbin.org/delete', data=payload, method='DELETE')
# with urllib.request.urlopen(req) as f:
#     r = json.loads(f.read().decode('utf-8'))
#     print(r)
