from django.shortcuts import render
from journal.models import Post
from django.http import HttpRequest

# Create your views here.


def index(request: HttpRequest):
    qs = Post.objects.all()
    return render(request, "journal/journal_list.html", {"journal_list": qs,})


def journal_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "journal/journal_detail.html", {"post": post,})

