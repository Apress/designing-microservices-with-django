import json

from django.core.management.base import BaseCommand, CommandError

from pizza.models import Likes
from pizza.utils.consumer import consumer


class Command(BaseCommand):
    help = "Consumes user deleted message from RabbitMQ"

    def _callback(self, channel, method, properties, body):
        payload = json.loads(body)
        user_id = payload.get('user_id')
        if user_id is not None:
            likes = Likes.objects.filter(user_id=user_id)
            likes.delete()

    def handle(self, *args, **options):
        consumer.consume(
            exchange='users',
            queue_name='users-deleted',
            routing_key='user.deleted',
            callback=self._callback,
        )
