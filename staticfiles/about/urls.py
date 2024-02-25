from django.urls import path
from .views import AboutPageView

app_name = "about"


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
]
