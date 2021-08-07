from movie import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    # path("actor/<int:pk>>/", views.actor_detail, name="actor_detail"),
    path("new/", views.movie_new, name="movie_new"),
]
