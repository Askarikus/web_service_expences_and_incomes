import os
import smtplib
from email.message import EmailMessage


def send_mail(subject, content, mail_from, mail_to):

    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = mail_from
    msg['To'] = mail_to

    # server

    server = smtplib.SMTP(host=os.environ.get('EMAIL_HOST'))
    server.connect(host=os.environ.get('EMAIL_HOST'), port=int(os.environ.get('EMAIL_PORT')))
    server.ehlo()
    server.starttls()
    server.login(os.environ.get('EMAIL_HOST_USER'), os.environ.get('EMAIL_HOST_PASSWORD'))
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    send_mail('S', 'C', 'askarikus23@gmail.com', 'askarikus@list.ru')
