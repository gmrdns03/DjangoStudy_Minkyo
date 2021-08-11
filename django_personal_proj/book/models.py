from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 상속을 위한 준비/abstract=True를 선언하면 가상의 클래스가 된다.
    class Meta:
        abstract = True


class Book(TimestampModel):
    title = models.CharField(max_length=30, unique=True)
    cover_img = models.ImageField()
    desc = models.TextField()
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = reverse("book_detail", args=[self.pk])
        return url


class Writer(TimestampModel):
    book = models.ForeignKey(Book, on_delete=CASCADE)
    name = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Review(TimestampModel):
    book = models.ForeignKey(Book, on_delete=CASCADE)
    message = models.TextField()


class Video(TimestampModel):
    Book = models.ForeignKey(Book, on_delete=CASCADE)
    youtube_url = models.URLField()
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title


class Tag(TimestampModel):
    book = models.CharField(max_length=10, blank=True)
    tag = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return self.tag

