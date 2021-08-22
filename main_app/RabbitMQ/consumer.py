import json
import sys

import pika
import requests

from xsolla_backend_2021.settings import QUEUE_TTL


def callback(ch, method, properties, body):
    """Обработка входящих сообщений"""
    body = json.loads(body)
    print(f'Received {body}')

    r = requests.get(body['landing'])
    if r.status_code == 200:
        # Подтверждение обработки сообщения
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        ch.basic_reject(delivery_tag=method.delivery_tag, multiple=False)


def main():
    # Подключение к rabbit
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Создание очереди
    channel.queue_declare(queue='landing', arguments={
        'x-message-ttl': QUEUE_TTL,  # ограничиваем время жизни
    })

    # Создание консьюмера
    channel.basic_consume(queue='landing', on_message_callback=callback, auto_ack=False)

    print('--Waiting for messages. To exit press CTRL+C--')

    # Ожидание сообщений
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')

        quit()
