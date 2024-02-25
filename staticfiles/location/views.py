from django.views.generic import ListView
from .models import Loc


class LocListView(ListView):
    model = Loc
    template_name = "location.html"
    context_object_name = "Loc"
