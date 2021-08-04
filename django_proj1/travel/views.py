from django.shortcuts import render
from travel.models import Post
from django.http import HttpRequest

# Create your views here.

# HttpRequest
#
# 현재 요청 내역 : 요청자의 IP, 브라우저/OS종류
# Form 내역 : username, pw, 글제목, 글내용, 업로드파일 등등


def index(request: HttpRequest):
    qs = Post.objects.all()  # QuerySet : 데이터베이스로의 쿼리를 생성/실행
    return render(
        request,
        "travel/post_list.html",
        {
            "post_list": qs,
        },
    )


def post_detail(request: HttpRequest, pk: int):  # pk는 프라이머리키의 약자
    post = Post.objects.get(pk=pk)
    return render(
        request,
        "travel/post_detail.html",
        {
            "post": post,
        },
    )
