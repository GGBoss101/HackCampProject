from django.urls import path
from . import views

urlpatterns = [
    path("", views.moodChooser, name="Mood Chooser"),
]