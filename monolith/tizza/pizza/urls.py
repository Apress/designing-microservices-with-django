from django.urls import include, path

from .views import index, GetTenPizzasView


urlpatterns = [
    path('<int:pid>', index),
    path('ten', GetTenPizzasView.as_view()),
]
