from movie.models import Actor, Movie, Video, Review
from movie.forms import MovieForm, ActorForm, ReviewForm, VideoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.http import JsonResponse

# 영화 목록, 디테일, 추가, 수정, 삭제
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


def movie_new(request: HttpRequest, pk):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            # return redirect(f"/movie/{movie.pk }/")
            # return redirect("movie_detail", pk)
            return redirect(movie)

    else:  # "GET"으로 받는 경우
        form = MovieForm()

    return render(request, "movie/movie_form.html", {"form": form,},)


def movie_edit(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save()
            # return redirect(f"/movie/{pk}/")
            return redirect("movie_detail", pk)
    else:
        form = MovieForm(instance=movie)

    return render(request, "movie/movie_form.html", {"form": form,},)


def movie_delete(request: HttpRequest, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()
        # return redirect(f"/movie/")
        return redirect("index")

    return render(request, "movie/movie_confrim_delete.html", {"movie": movie,},)


# 배우 목록, 디테일, 추가 (수정, 삭제)
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


# 강사님꺼 코드
@login_required
def review_list(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    # review_list = movie.review_set.all()

    review_list = Review.objects.filter(movie__pk=movie_pk)

    # python plain objects로 변환
    # JSON으로 변환하는 파이썬 기본 라이브러리인 json.dumps를 통해서 이뤄집니다.
    #  파이썬 기본 타입에 대해서만 변환 룰을 제공해줍니다.
    #  추가 타입에 대해서는? 커스텀 Rule을 지정할 수 있습니다. => json.dumps에 cls 인자를 통해 가능
    response_data = [
        {
            "message": review.message,
            "edit_url": resolve_url("review_edit", movie_pk, review.pk),
            "delete_url": resolve_url("review_delete", movie_pk, review.pk),
            "author": {"username": review.author.username,},
        }
        for review in review_list
    ]
    return JsonResponse(
        response_data, safe=False, json_dumps_params={"ensure_ascii": False}
    )

    # # 우리가 일반적인 응답 포맷은 HTML
    # return render(request, "movist/review_list.html", {
    #     "review_list": review_list,
    # })


# 영화 리뷰 추가, 수정, 삭제
@login_required
def review_new(request: HttpRequest, movie_pk: int):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review: Review = form.save(commit=False)
            review.movie = movie
            review.author = request.user
            review.save()
            # return redirect(f"/movie/{movie_pk}")
            return redirect(review.movie)

    else:  # GET 방식으로 받은 경우
        form = ReviewForm()

    return render(request, "movie/review_form.html", {"form": form,},)


@login_required
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


@login_required
def review_delete(request: HttpRequest, movie_pk: int, pk: int):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect(f"/movie/{movie_pk}/")

    return render(request, "movie/review_confirm_delete.html", {"review": review,},)


# 비디오 추가, 수정, 삭제
def video_new(request: HttpRequest, movie_pk: int):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.movie = movie
            video.save()
            return redirect(f"/movie/{movie_pk}/")

    else:
        form = VideoForm()

    return render(request, "movie/video_form.html", {"movie": movie, "form": form,},)


def video_edit(request: HttpRequest, movie_pk: int, pk: int) -> HttpResponse:
    video = Video.objects.get(pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            video = form.save()
            return redirect(f"/movie/{movie_pk}/")

    else:
        form = VideoForm(instance=video)
    # instance를 안넣어주면 수정 화면에서 본래의 텍스트가 표출이 안된다.

    return render(request, "movie/video_form.html", {"form": form,},)


def video_delete(request: HttpRequest, movie_pk: int, pk: int) -> HttpResponse:
    video = Video.objects.get(pk=pk)
    if request.method == "POST":
        video.delete()
        return redirect(f"/movie/{movie_pk}")

    return render(request, "movie/video_confirm_delete.html/", {"video": video,},)
