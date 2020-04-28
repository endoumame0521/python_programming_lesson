# SMTPハンドラーでログをEmail送信（Hot mailの場合）

import logging
import logging.handlers


# メールの設定
smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxxx@hotmail.com'
to_email = 'yyyy@hotmail.com'
user_name = 'tanakasan'
password = 'fsflksdfsdfk,'

logger = logging.getLogger('email')

# ログを送るレベルをcriticalに設定
logger.setLevel(logging.CRITICAL)

# ログをメールで送る
logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log',
    credentials=(user_name, password),
    secure=(None, None, None),
    timeout=20
))

logger.info('test')
logger.critical('critical')

