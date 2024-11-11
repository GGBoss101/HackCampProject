from django.shortcuts import render
from moodchooser.models import MoodEntry
# Create your views here.

def home(response):

    all_mood_entries = MoodEntry.objects.all
    return render(response, "home.html", {"moods":all_mood_entries})