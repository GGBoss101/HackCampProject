from django.shortcuts import render
from moodchooser.models import MoodEntry
# Create your views here.

def home(response):

    all_mood_entries = MoodEntry.objects.all()
    moods_by_day = {}

    for item in all_mood_entries:
        moods_by_day.update({item.date.strftime('%a').upper() : item.mood})

    return render(response, "home.html", {"moods":moods_by_day})

