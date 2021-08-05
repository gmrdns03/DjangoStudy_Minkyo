from journal.models import Post
from journal.models import Journalist
from journal.models import Comment
from django.contrib import admin

# Register your models here.


@admin.register(Journalist)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "created_at", "updated_at"]
    list_filter = ["created_at"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["photo", "title", "journalist", "created_at"]
    list_filter = ["created_at"]


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["post"]
    list_display = ["post", "message", "created_at"]
    list_filter = ["created_at"]

