from django.shortcuts import render
from .movies import movies_data

# Create your views here.
def home(request):
    movies = movies_data
    return render(request, 'home.html', {'movies': movies})