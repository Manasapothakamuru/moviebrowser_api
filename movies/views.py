from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

# New view for the root URL
def home(request):
    return HttpResponse("Welcome to the Movie App API. Use /api/movies/ to access the movie list.")

# Existing views
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
