# Register your models here.
from django.contrib import admin

from .models import Blog, Post, gen_word


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title']
    ordering = ['title']
    prepopulated_fields = {"slug": ("title",)}


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "blog", "created", "intro_body"]
    ordering = ["-id"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
