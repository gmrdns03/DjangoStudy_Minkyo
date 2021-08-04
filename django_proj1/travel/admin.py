from django.contrib import admin
from travel.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "message", "latitude", "longitude"]
