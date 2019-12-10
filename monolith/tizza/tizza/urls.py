from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView

from pizza.routers import router as pizza_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzas/', include('pizza.urls')),

    path('user/', include('user.urls')),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('', include(pizza_router.urls)),
]
