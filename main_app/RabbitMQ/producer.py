from json import dumps

import pika
from django.forms.models import model_to_dict

from main_app.models import Product


def check_landing(product: Product):
    """Проверка лендинга товара"""
    product_dict = model_to_dict(product)
    serialized_product = dumps(product_dict)

    # Установка соединения с rabbit
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Определение очереди
    channel.queue_declare(queue='landing')

    # Отправка сообщения
    channel.basic_publish(exchange='', routing_key='landing', body=serialized_product)

    print(f'Sent {serialized_product}')
    connection.close()
