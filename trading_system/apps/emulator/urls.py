from django.urls import path
from apps.emulator import views

urlpatterns = [
    path("", views.index, name="index")
]
