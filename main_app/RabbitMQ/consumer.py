import json
import time

import pika
import requests

"""КОНСЬЮМЕР"""
QUEUE_TTL = 5000  # Время жизни запроса

RECHECK_TIME = 1  # Время перепроверки лендинга, если запрос вернул неудачу (в минутах)


def callback(ch, method, properties, body):
    """Обработка входящих сообщений"""
    json_body = json.loads(body)
    print(f'Received {json_body}')

    r = requests.get(json_body['landing'])
    print(r.status_code)
    if 200 <= r.status_code < 300:
        # Подтверждение получения лендинга
        print('success check')
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        # Получить лендинг не удалось
        print('failed check')
        ch.basic_ack(delivery_tag=method.delivery_tag)

        # повторная отправка сообщения с задержкой
        ch.basic_publish(exchange='landing-exchange',
                         routing_key='landing',
                         properties=pika.BasicProperties(
                             headers={'x-delay': RECHECK_TIME * 1000}),  # время задержки в мс
                         body=body)


def main():
    # Подключение к rabbit
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    # Определяем обменник
    channel.exchange_declare(exchange='landing-exchange',
                             exchange_type='x-delayed-message',
                             arguments={"x-delayed-type": "direct"})
    # Создание очереди
    channel.queue_declare(queue='landing')

    channel.queue_bind(exchange='landing-exchange',
                       queue='landing',
                       routing_key='landing')
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
