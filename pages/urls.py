from django.urls import path
from .views import HomePageView, AboutPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"), #homepage.com/
    path("about/", AboutPageView.as_view(), name="about"), #homepage.com/about/
]