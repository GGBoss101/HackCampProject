from django.shortcuts import render

# Create your views here.

def moodChooser(request):

    return render(request, "moodchooser.html")