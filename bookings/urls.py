"""
Bookings App - URLS
----------------
URLS configuration for Bookings App

"""
from . import views
from django.urls import path

urlpatterns = [
    path('/bookings', views.Booking.as_view(), name='bookings'),
]
