from django.urls import path

from .views import SignupView


urlpatterns = [
    path('register', SignupView.as_view()),
]
