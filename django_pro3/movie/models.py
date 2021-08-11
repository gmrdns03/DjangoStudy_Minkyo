from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields import URLField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Actor(TimestampedModel):
    name = models.CharField(max_length=20)
    photo = models.ImageField()
    # many to many로 Movie와 연결하는 방법 찾아보기

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "주연배우"
        verbose_name_plural = "주연배우 목록"


class Movie(TimestampedModel):
    title = models.CharField(max_length=30)
    poster = models.ImageField()
    desc = models.TextField()
    director = models.CharField(max_length=20)
    actor = models.ForeignKey(Actor, on_delete=CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = reverse("movie_detail", args=[self.pk])
        return url


class Video(TimestampedModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    youtube_url = models.URLField()

    def __str__(self):
        return self.name


class Review(TimestampedModel):
    author = models.ForeignKey(User, on_delete=CASCADE)
    movie = models.ForeignKey(Movie, on_delete=CASCADE)
    message = models.TextField()


# class Video(TimestampedModel):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     youtube_url = models.URLField()

#     # 인자없는 멤버함수는 속성처럼 사용하고 싶습니다.
#     @property
#     def youtube_id(self):
#         # https://www.youtube.com/watch?v=xyfozmk1SxQ
#         if "v=" in self.youtube_url:
#             return self.youtube_url.split("v=")[1]
#         return None

#     @property
#     def youtube_embed_html(self):
#         if self.youtube_id:
#             return render_to_string(
#                 "movist/_youtube_embed.html", {"youtube_id": self.youtube_id,}
#             )
#         return None
