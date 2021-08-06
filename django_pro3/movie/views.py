from movie.models import Actor, Movie, Video, Review
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request: HttpRequest):
    qs = Movie.objects.all()
    return render(request, "movie/movie_list.html", {"movie_list": qs,},)


# def index(request):
#     qs = Movie.objects.all()
#     return render(request, "movie/movie_list.html", {"movie_list": qs,},)

