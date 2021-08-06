from movie.models import Actor, Movie, Video, Review
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request: HttpRequest):
    qs = Movie.objects.all()
    return render(request, "movie/movie_list.html", {"movie_list": qs,},)


def movie_detail(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    review_list = movie.review_set.all()
    return render(
        request,
        "movie/movie_detail.html",
        {"movie": movie, "review_list": review_list,},
    )

