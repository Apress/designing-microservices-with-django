from django.contrib import admin

from .models import Team, Owner, Service


class TeamAdmin(admin.ModelAdmin):
    pass


class OwnerAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Team, TeamAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Service, ServiceAdmin)
