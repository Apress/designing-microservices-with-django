from django.http import HttpResponse

from .models import Pizza


def random(request, pid):
    pizza = Pizza.objects.order_by('?')[0]
    return HttpResponse(
        content={
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        }
    )