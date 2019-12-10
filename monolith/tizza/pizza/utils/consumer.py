import os
import pika


class Consumer:

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def _init_channel(self):
        connection = pika.BlockingConnection(
            pika.URLParameters(f'amqp://{self.username}:{self.password}@{self.host}:5672')
        )
        return connection.channel()

    def _init_queue(self, channel, exchange, queue_name, routing_key):
        channel.queue_declare(queue=queue_name)
        channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
        return queue_name

    def consume(self, exchange, queue_name, routing_key, callback):
        channel = self._init_channel()
        queue_name = self._init_queue(channel, exchange, queue_name, routing_key)
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
        )


consumer = Consumer(
    host=os.environ.get('RABBITMQ_HOST'),
    username=os.environ.get('RABBITMQ_USERNAME'),
    password=os.environ.get('RABBITMQ_PASSWORD'),
)
