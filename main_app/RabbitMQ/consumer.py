import json
import time

import pika
import requests

"""КОНСЬЮМЕР"""
QUEUE_TTL = 5000  # Время жизни запроса

RECHECK_TIME = 1  # Время перепроверки лендинга, если запрос вернул неудачу (в минутах)


def callback(ch, method, properties, body):
    """Обработка входящих сообщений"""
    body = json.loads(body)
    print(f'Received {body}')

    r = requests.get(body['landing'])
    if 300 <= r.status_code < 300:
        # Подтверждение получения лендинга
        print('success check')
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        # Получить лендинг не удалось
        print('failed check')
        ch.basic_reject(delivery_tag=method.delivery_tag)
        time.sleep(RECHECK_TIME * 60)


def main():
    # Подключение к rabbit
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Создание очереди
    channel.queue_declare(queue='landing')

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
