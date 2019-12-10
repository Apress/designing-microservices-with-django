from django.http import HttpResponse


def index(request, pid):
    try:
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse(
            content={
                'id': pizza.id,
                'title': pizza.title,
                'description': pizza.description,
            }
        )
    except ObjectDoesNotExist:
        return HttpResponse(
            status_code=404,
            content={
                'status': 'error',
                'message': 'pizza not found',
            }
        )
