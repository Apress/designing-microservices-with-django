from rest_framework import viewsets

from .models import Pizza, Pizzeria
from .serializers import PizzaSerializer, PizzeriaSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzeriaViewSet(viewsets.ModelViewSet):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaSerializer
