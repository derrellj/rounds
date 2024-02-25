from django.contrib import admin
from .models import AboutPost


class AboutPostAdmin(admin.ModelAdmin):
    model = AboutPost
    list_display = ("display_text", "image")

    def display_text(self, obj):
        return obj.text[:50]

    display_text.short_description = "Text"


admin.site.register(AboutPost, AboutPostAdmin)
