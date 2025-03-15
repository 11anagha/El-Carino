from django.shortcuts import render
from user import models

# Create your views here.
def home(request):
    bookings = models.Booking.objects.all()

    context = {
        "bookings": bookings
    }
    return render(request, "admin_panel/home.html", context=context)



def stream(request):
    return render(request, "admin_panel/stream.html")



def live_event(request, stream_id):
    return render(request, "admin_panel/viewer.html", {"stream_id": stream_id})