from django.urls import path
from journal import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.journal_detail, name="journal_detail"),
]

