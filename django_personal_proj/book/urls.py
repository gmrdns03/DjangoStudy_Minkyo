from book import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="book_list"),
]
