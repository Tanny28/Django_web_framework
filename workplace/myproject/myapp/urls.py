from django.urls import path
from .views import booking_view  # Ensure the correct view function is imported

urlpatterns = [
    path("booking/", booking_view, name="booking"),  # Define the booking route
]
