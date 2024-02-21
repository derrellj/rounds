from django.contrib import admin

from .models import Service


class SerivceAdmin(admin.ModelAdmin):
    model = Service
    list_display = [
        "service",
        "name",
        "price",
    ]


admin.site.register(Service, SerivceAdmin)
