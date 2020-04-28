# メールを添付ファイル付きで送信（Hot mailの場合）

from email import message
from email.mime import multipart
from email.mime import text
import smtplib


# メールの設定
smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxxx@hotmail.com'
to_email = 'yyyy@hotmail.com'
user_name = 'tanakasan'
password = 'fsflksdfsdfk,'

# メッセージを作成
# msg = message.EmailMessage()
msg = multipart.MIMEMultipart()
# メッセージの本文を定義
# msg.set_content('test email')
# メッセージの表題を定義
msg['Subject'] = 'Test email sub'
# メッセージの送信者を定義
msg['From'] = from_email
# メッセージの宛先を定義
msg['To'] = to_email

msg.attach(text.MIMEText('Test email', 'plain'))

with open('lesson.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment', filename='lesson.text'
    )
    msg.attach(attachment)

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
