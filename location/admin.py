from django.contrib import admin

from .models import Loc


class LocAdmin(admin.ModelAdmin):
    model = Loc
    list_display = ["text"]


admin.site.register(Loc)
