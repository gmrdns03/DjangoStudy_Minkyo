from django.shortcuts import render
from shop.models import Item
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):  # pk는 프라이머리키의 약자
    qs = Item.objects.all()  # QuerySet
    return render(request, "shop/item_list.html", {"item_list": qs,},)


def item_detail(request, pk: int):
    item = Item.objects.get(pk=pk)
    return render(request, "shop/item_detail.html", {"item": item,})

