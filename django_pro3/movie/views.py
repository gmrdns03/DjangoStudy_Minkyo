from movie.models import Actor, Movie, Video, Review
from movie.forms import MovieForm, ActorForm, ReviewForm

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request: HttpRequest):
    qs = Movie.objects.all()
    return render(request, "movie/movie_list.html", {"movie_list": qs,},)


def movie_detail(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    review_list = movie.review_set.all()
    video_list = movie.video_set.all()
    return render(
        request,
        "movie/movie_detail.html",
        {"movie": movie, "review_list": review_list, "video_list": video_list,},
    )


def movie_new(request: HttpRequest):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect(f"/movie/{movie.pk }")

    else:  # "GET"으로 받는 경우
        form = MovieForm()

    return render(request, "movie/movie_form.html", {"form": form,},)


def movie_edit(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect(f"/movie/{pk}/")
    else:
        form = MovieForm(instance=movie)

    return render(request, "movie/movie_form.html", {"form": form,},)


def movie_delete(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect(f"/movie/")

    return render(request, "movie/movie_confrim_delete.html", {"movie": movie,},)


def actor_index(request: HttpRequest) -> HttpResponse:
    qs = Actor.objects.all()
    return render(request, "movie/actor_list.html", {"actor_list": qs,},)


def actor_detail(request: HttpRequest, actor_pk) -> HttpResponse:
    actor = Actor.objects.get(pk=actor_pk)
    movie_list = actor.movie_set.all()
    return render(
        request, "movie/actor_detail.html", {"actor": actor, "movie_list": movie_list,},
    )


def actor_new(request: HttpRequest):
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            actor = form.save()
            return redirect(f"/movie/actor/{actor.pk}/")

    else:
        form = ActorForm()

    return render(request, "movie/actor_form.html", {"form": form,},)


def review_new(request: HttpRequest, movie_pk: int):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect(f"/movie/{movie_pk}")

    else:  # GET 방식으로 받은 경우
        form = ReviewForm()

    return render(request, "movie/review_form.html", {"form": form,},)


def review_edit(request: HttpRequest, movie_pk: int, pk: int):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(f"/movie/{movie_pk}/")

    else:
        form = ReviewForm(instance=review)

    return render(request, "movie/review_form.html", {"form": form,},)


def review_delete(request: HttpRequest, movie_pk: int, pk: int):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect(f"/movie/{movie_pk}/")

    return render(request, "movie/review_fonfirm_delete.html", {"review": review,},)
