from json import dumps

import pika
from django.forms.models import model_to_dict

from main_app.RabbitMQ.consumer import QUEUE_TTL
from main_app.models import Product

"""ПРОДЮСЕР"""


def check_landing(product: Product):
    """Проверка лендинга товара"""
    product_dict = model_to_dict(product)

    # кодируем созданный продукт в строку json
    serialized_product = dumps(product_dict).encode()

    # Установка соединения с rabbit
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='landing-exchange',
                             exchange_type='x-delayed-message',
                             arguments={"x-delayed-type": "direct"})
    # Определение очереди
    # channel.queue_declare(queue='landing')

    # Отправка сообщения
    channel.basic_publish(exchange='landing-exchange', routing_key='landing', body=serialized_product,
                          properties=pika.BasicProperties(expiration=str(QUEUE_TTL)))

    print(f'Sent {serialized_product}')

    connection.close()
