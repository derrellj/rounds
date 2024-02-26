from django.urls import path
from .views import HomePostView

app_name = "pages"


urlpatterns = [
    path("", HomePostView.as_view(), name="home"),
]
