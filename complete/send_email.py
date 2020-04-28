# メールの送信方法（Hot mailの場合）

from email import message
import smtplib


# メールの設定
smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxxx@hotmail.com'
to_email = 'yyyy@hotmail.com'
user_name = 'tanakasan'
password = 'fsflksdfsdfk,'

# メッセージを作成
msg = message.EmailMessage()
# メッセージの本文を定義
msg.set_content('test email')
# メッセージの表題を定義
msg['Subject'] = 'Test email sub'
# メッセージの送信者を定義
msg['From'] = from_email
# メッセージの宛先を定義
msg['To'] = to_email

# SMTPサーバーを作成
server = smtplib.SMTP(smtp_host, smtp_port)
# SMTPサーバーとのやりとりを開始
server.ehlo()
# セキュアな通信をする
server.starttls()
# SMTPサーバーとのやりとりを開始
server.ehlo()
# SMTPサーバーにログイン
server.login(username, password)
# メールを送信
server.send_message(msg)
# SMTPサーバーとのやりとりを停止
server.quit()
