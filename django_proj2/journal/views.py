from journal.models import Post, Comment
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from journal.forms import PostForm, CommentForm
from django.shortcuts import redirect, render

# from journal.forms import


# Create your views here.


def index(request: HttpRequest):
    qs = Post.objects.all()
    return render(request, "journal/journal_list.html", {"journal_list": qs,})


# index = ListView.as_view(model=Post)


def journal_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment_list = post.comment_set.all()
    return render(
        request,
        "journal/journal_detail.html",
        {"post": post, "comment_list": comment_list},
    )


def post_new(request: HttpRequest):
    if request.method == "GET":
        form = PostForm()
    else:  # POST
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=Fals를 지정하면, post.saver()가 호출되지 않음
            # post 인스턴스를 반환
            post = form.save(commit=False)  # 방금 저장한 모델 객체를 반환
            post.ip = request.META["REMOTE_ADDR"]
            post.save()
            return redirect(f"/journal/{post.pk}/")

    return render(request, "journal/post_form.html", {"form": form,},)


def post_edit(request: HttpRequest, pk):
    post = Post.objects.get(pk=pk)

    if request.method == "GET":
        form = PostForm(instance=post)
    else:  # POST
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META["REMOTE_ADDR"]
            post.save()  # 방금 저장한 모델 객체를 반환
            return redirect(f"/journal/{post.pk}/")

    return render(request, "journal/post_form.html", {"form": form,},)


def comment_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    post = Post.objects.get(pk=post_pk)
    # 댓글쓰기에 성공하면 post detail로 이동
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=Fals를 지정하면, post.saver()가 호출되지 않음
            # post 인스턴스를 반환
            comment = form.save(commit=False)  # 방금 저장한 모델 객체를 반환
            comment.post = post
            comment.save()
            return redirect(f"/journal/{post_pk}/")
    else:
        form = CommentForm()
    return render(request, "journal/comment_form.html", {"form": form,},)


def comment_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    # 댓글쓰기에 성공하면 post detail로 이동
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(f"/journal/{post_pk}/")

    else:
        form = CommentForm(instance=comment)

    return render(request, "journal/comment_form.html", {"form": form,},)


def comment_delete(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        comment.delete()
        return redirect(f"/journal/{post_pk}/")

    return render(request, "journal/comment_fonfirm_delete.html", {"comment": comment},)
