from django.contrib import admin

from places.models import Post, Pic


class PicsInline(admin.TabularInline):
    model = Pic
    readonly_fields = ["photo_preview"]

    def photo_preview(self, obj):
        return obj.photo_preview

    photo_preview.short_description = 'Photo Preview'
    photo_preview.allow_tags = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ["title", "description_short", "description_long", "lat", "lon", "point_lon", "point_lat", "slug"]
    list_display = ['pk', 'title']
    inlines = [PicsInline, ]


@admin.register(Pic)
class PicAdmin(admin.ModelAdmin):
    list_display = ['numb', "title", "photo_preview"]
    ordering = ['numb', ]
    readonly_fields = ["photo_preview"]

    def photo_preview(self, obj):
        return obj.photo_preview

    photo_preview.short_description = 'Photo Preview'
    photo_preview.allow_tags = True
