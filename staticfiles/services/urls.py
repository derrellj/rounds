from django.urls import path
from .views import ServicePageView

app_name = "services"


urlpatterns = [
    path("service/", ServicePageView.as_view(), name="service"),
]
