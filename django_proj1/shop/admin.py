from shop.models import Review
from django.contrib import admin
from shop.models import Item

# Register your models here.


@admin.register(Item)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "desc", "price", "is_public", "created_at", "updated_at"]
    list_filter = ["is_public", "created_at"]


@admin.register(Review)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["item"]
    list_display = ["item", "message", "created_at", "updated_at"]

