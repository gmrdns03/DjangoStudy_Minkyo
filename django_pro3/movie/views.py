from movie.models import Actor, Movie, Video, Review
from movie.forms import MovieForm, ActorForm

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


def actor_index(request: HttpRequest):
    qs = Actor.objects.all()
    # movie_list = qs.movie_set.all()
    return render(request, "movie/actor_list.html", {"actor_list": qs,},)


def actor_detail(request: HttpRequest, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    movie_list = actor.movie_set.all()
    return render(
        request, "movie/actor_detail.html", {"actor": actor, "movie_list": movie_list,},
    )


def movie_new(request: HttpRequest):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect(f"/movie/{movie.pk }")

    else:  # "GED"으로 받는 경우
        form = MovieForm()

    return render(request, "movie/movie_form.html", {"form": form,},)


# def actor_new(request: HttpRequest):
#     if request.method = "POST":
#         form = ActorForm(request.POST, request.FILES)
#         if form.is_valid():
#             actor = form.save()
#             actor.save()
#             return redirect(f"/movie")

