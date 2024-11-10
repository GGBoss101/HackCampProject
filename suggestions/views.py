from django.shortcuts import render

# Create your views here.

def suggestions(request):
    return render(request, "suggestionpage.html")