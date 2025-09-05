import base64
from email.mime.text import MIMEText
from gmailauth import gmail_authenticate
import email

def send_email(subject, message_text, to_email):
    service = gmail_authenticate()
    message = MIMEText(message_text)
    message['to'] = to_email
    message['subject'] = subject

    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    send_message = service.users().messages().send(userId="me", body=create_message).execute()
    print(f"Message Id: {send_message['id']}")

def list_messages(max_results=5):
    service = gmail_authenticate()
    result = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = result.get('messages', [])
    return messages

def read_message(message_id):
    service = gmail_authenticate()
    msg = service.users().messages().get(userId='me', id=message_id, format='full').execute()
    payload = msg['payload']
    headers = payload['headers']
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), None)
    from_email = next((h['value'] for h in headers if h['name'] == 'From'), None)

    parts = payload.get('parts')
    if parts:
        data = parts[0]['body']['data']
    else:
        data = payload['body']['data']

    decoded_data = base64.urlsafe_b64decode(data.encode('UTF-8')).decode('utf-8')
    print(f"From: {from_email}")
    print(f"Subject: {subject}")
    print("Message:")
    print(decoded_data)
