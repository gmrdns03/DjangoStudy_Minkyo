from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from book.models import Book

# Create your views here.
def index(request: HttpRequest):
    qs = Book.objects.all()
    return render(request, "book/book_list.html", {"book_list": qs,},)
