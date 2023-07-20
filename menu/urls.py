"""
Menu App - URLS
----------------
Urls Configuration for Menu App.
"""
from django.urls import path
from . import views


urlpatterns = [
    path("menu/", views.Menu.as_view(), name="menu"),
]
