from django.contrib import admin

# Register your models here.
# a new import
from .models import Post, Category

# and a new admin registration
admin.site.register(Post)
admin.site.register(Category)               # <-- Register Category
