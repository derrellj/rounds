from django.views.generic import ListView
from .models import AboutPost


class AboutPageView(ListView):
    model = AboutPost
    template_name = "about.html"
    context_object_name = "about"
