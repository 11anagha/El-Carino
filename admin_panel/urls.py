from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="admin_home"),
    path("stream/", views.stream, name="stream"),
    path("live-event/", views.live_event, name="live_event"),
]