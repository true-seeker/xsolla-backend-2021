import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(data):
    """Отправка письма"""
    print('mailer started')
    data = json.loads(data)

    msg = MIMEMultipart()

    message = f"Вы успешно приобрели товар {data['product_title']}"

    password = ""
    msg['From'] = "murzinkirill5667@gmail.com"
    msg['To'] = data['send_to']
    msg['Subject'] = "Покупка товара Xsolla"
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    info = f'successfully sent email to {data["send_to"]}:'
    print(info)
    return info
