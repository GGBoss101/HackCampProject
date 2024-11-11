from django.urls import path
from . import views

app_name = 'moodchooser'

urlpatterns = [
    path("chooser/", views.moodChooser, name='mood_chooser'),
]