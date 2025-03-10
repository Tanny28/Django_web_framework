from django.shortcuts import render
from .forms import BookingForm  # Ensure the BookingForm is imported

def booking_view(request):
    form = BookingForm()
    return render(request, "booking.html", {"form": form})
