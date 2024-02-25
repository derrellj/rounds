from django.views.generic import ListView
from .models import Service


class ServicePageView(ListView):
    model = Service
    template_name = "services.html"
    context_object_name = "Service"
