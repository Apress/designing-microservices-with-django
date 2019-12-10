import json
import pika
import sys

from django.conf import settings


class Producer:
    
    def __init__(self, host, username, password):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(f'amqp://{username}:{password}@{host}:5672')
        )
        self.channel = connection.channel()
        self.exchanges = []

    def produce(self, exchange, body, routing_key=''):
        if exchange not in self.exchanges:
            self.channel.declare_exchange(exchange=exchange)
            self.exchanges.append(exchange)
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(body),
        )


producer = Producer(
    host=os.environ.get('RABBITMQ_HOST'),
    username=os.environ.get('RABBITMQ_USERNAME'),
    password=os.environ.get('RABBITMQ_PASSWORD'),
)
