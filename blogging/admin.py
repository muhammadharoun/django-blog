from django.contrib import admin

# Register your models here.
# a new import
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]

