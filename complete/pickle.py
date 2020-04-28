"""
pickleとは
・pythonのコードで書いた内容をそのまま外部ファイル(.pickle)に
　書き出したり読み出したりする事ができるライブラリ。
・データベースではない。あくまで外部ファイルに保存しているだけ。
・使用用途はpython内だけがいい。なぜなら他の言語とは互換性がないから。
　その点、データベースは他の言語とも互換性がある。
"""

import pickle

# 確認用に適当にクラスを定義
class T(object):
    def __init__(self, name):
        self.name = name


# 確認用に適用に辞書を定義
data = {
    'a': [1, 2, 3],
    'b': ('test', 'test'),
    'c': {'test', 'test'},
    'd': T('test'),
}

# wb...write binary（バイナリ形式で書き込み）
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# rb...read binary（バイナリ形式で読み込み）
with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
    print(type(data_loaded['d']))
