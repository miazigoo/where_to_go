from django.contrib import admin

from places.models import Post, Pic


class PicsInline(admin.TabularInline):
    model = Pic


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [PicsInline, ]


@admin.register(Pic)
class PostAdmin(admin.ModelAdmin):
    list_display = ['numb', 'title']
    ordering = ['numb', ]
