import string
import random

from Crypto.Cipher import AES

# 変数keyにascii_letters(abcdef...VWXYZ)からAES.block_size(デフォルト値16)個
# ランダムに取り出した文字列を入れる
key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size))

# 初期ベクトル
iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size))

with open('plaintext', 'r') as f, open('enc.dat', 'wb') as e:
    # 暗号化する文字列をテキストファイルから読み込む
    plaintext = f.read()
    # 暗号化のモードを設定（ここではCBCモード）
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 暗号化する際にブロックサイズに足りなかった文字数だけ文字を付与する
    padding_length = AES. block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    # 暗号化
    cipher_text = cipher.encrypt(plaintext)
    e.write(cipher_text)

# 暗号化されたファイルを復号化する為に読み込む
with open('enc.dat', 'rb') as f:
    # 復号化するモードを設定
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    # 復号化
    decrypted_text = cipher2.decrypt(f.read())

    # 暗号化される直前の文字列を表示
    print(decrypted_text)
    # 暗号化される前付与された文字列を表示
    print(decrypted_text[-1])
    # 元の文字列を表示
    print(decrypted_text[:-decrypted_text[-1]].decode('utf-8'))
