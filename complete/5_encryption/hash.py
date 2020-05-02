import base64
import os
import hashlib


# print(hashlib.sha256(b'password').hexdigest())
# => 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
# password と言う文字列からsha256と言うアルゴリズムに渡してhexdigestして表示
# 逆に、元の password と言う文字列に戻すことはできない

user_name = 'user1'
user_pass = 'password'
db = {}

# base64形式でランダムな32文字を生成
salt = base64.b64encode(os.urandom(32))
# print('Salt: {}'.format(salt))


# 上記のuser_passで設定した文字列と上記のsaltを足し合わせた文字列をsha256でハッシュ化
# def get_digest(password):
#     password = bytes(password, 'utf-8')
#     digest = hashlib.sha256(salt + password).hexdigest()
    # さらにループを回してハッシュ化しまくる
    # for _ in range(5):
    #     digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
        # print(digest)
    # print('Digest: {}'.format(digest))
    # return digest


# 上記の get_digest関数と全く同じ
digest = hashlib.pbkdf2_hmac(
    'sha256', bytes(user_pass, 'utf-8'), salt, 10000)

# digest = get_digest(user_pass)

# dbにハッシュを保存
db[user_name] = digest
# db[user_name] = get_digest(user_pass)


# パスワードとユーザーネームが一位していればTrueを返す
def is_login(user_name, password):
    # return get_digest(password) == db[user_name]
    digest = hashlib.pbkdf2_hmac(
        'sha256', bytes(password, 'utf-8'), salt, 10000)
    return digest == db[user_name]


print(is_login(user_name, user_pass))
