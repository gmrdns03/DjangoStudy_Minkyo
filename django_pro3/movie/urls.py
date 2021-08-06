from movie import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
]
