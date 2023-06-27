from django.contrib import admin

from places.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
