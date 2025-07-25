from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/time/", views.current_time, name="current_time")
]