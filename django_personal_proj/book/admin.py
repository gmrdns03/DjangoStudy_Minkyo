from django.contrib import admin
from book.models import Book, Writer, Review, Video, Tag

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "cover_img", "publisher"]
    list_filter = ["title"]


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["photo", "name"]
    list_filter = ["name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ["book"]
    list_display = ["book", "message"]
    list_filter = ["book"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    search_fields = ["Book"]
    list_display = ["Book", "title", "youtube_url"]
    list_filter = ["Book"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
