from rest_framework import routers

from .viewsets import PizzaViewSet, PizzeriaViewSet


router = routers.DefaultRouter()
router.register('api/v1/pizzas', PizzaViewSet)
router.register('api/v1/pizzerias', PizzeriaViewSet)
