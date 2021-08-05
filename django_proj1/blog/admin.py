from django.contrib import admin

from blog.models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at"]
    list_display_links = ["title"]
    search_fields = ["title"]
