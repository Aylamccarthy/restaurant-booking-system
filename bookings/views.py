from django.views.generic import TemplateView


class Booking(TemplateView):
    template_name = "bookings.html"
