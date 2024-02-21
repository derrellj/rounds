from django.urls import path
from .views import LocListView

app_name = "location"


urlpatterns = [
    path("loc/", LocListView.as_view(), name="loc"),
]
