"""
ウェルノウンポート番号(0-1023)
登録済みポート番号(1024-49151)
動的・プライベート ポート番号(49152-65535)
"""


import socket

# TCPの場合
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # AF_INET はipv4という意味
#     s.bind(('127.0.0.1', 50007))
#     # １接続という意味
#     s.listen(1)
#     while True:
#         # 誰かが接続してきたらコネクションとアドレスを設定
#         conn, addr = s.accept()
#         with conn:
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print('data: {}, addr: {}'.format(data, addr))
#                 # コネクションが確立したらデータを接続してきたユーザに返す
#                 # バイトで返すのでbをつける
#                 conn.sendall(b'Received: ' + data)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr = s.recvfrom(1024)
        print('data: {}, addr: {}'.format(data, addr))
