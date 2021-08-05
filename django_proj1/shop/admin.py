from django.contrib import admin
from shop.models import Item

# Register your models here.


@admin.register(Item)
class PostAdmin(admin.ModelAdmin):
    list_display = ["name", "desc", "price", "is_public", "created_at", "updated_at"]
