from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, response
from book.models import Book, Review, Video, Writer, Tag

# Create your views here.
def index(request: HttpRequest):
    qs = Book.objects.all()
    return render(request, "book/book_list.html", {"book_list": qs,},)


# 북 디테일
def book_detail(request: HttpRequest, pk: int) -> HttpResponse:
    book = Book.objects.get(pk=pk)
    review_list = book.review_set.all()
    video_list = book.video_set.all()


# 북 수정
def book_edit(request: HttpRequest, pk: int) -> HttpResponse:
    pass


# 북 삭제
def book_delete(repuest: HttpRequest, pk: int) -> HttpResponse:
    pass


# 리뷰 쓰기
def review_new(request: HttpRequest, book_pk: int) -> HttpResponse:
    pass


# 리뷰 수정
def review_edit(request: HttpRequest, book_pk: int, pk: int) -> HttpResponse:
    pass


# 리뷰 삭제
def review_delete(request: HttpRequest, book_pk: int, pk: int) -> HttpResponse:
    pass


# 비디오 추가
def video_new(request: HttpRequest, book_pk: int) -> HttpResponse:
    pass


# 비디오 수정
def video_edit(request: HttpRequest, book_pk: int, pk: int) -> HttpResponse:
    pass


# 비디오 삭제
def video_delet(request: HttpRequest, book_pk: int, pk: int) -> HttpResponse:
    pass
