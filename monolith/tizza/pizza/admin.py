from django.contrib import admin

from .models import Pizza, Pizzeria, Likes


class PizzaAdmin(admin.ModelAdmin):
    pass


class PizzeriaAdmin(admin.ModelAdmin):
    pass


class LikesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pizzeria, PizzeriaAdmin)
admin.site.register(Likes, LikesAdmin)
