# メール一覧を取得
from mails import list_messages, read_message

messages = list_messages(3)
for msg in messages:
    read_message(msg['id'])
