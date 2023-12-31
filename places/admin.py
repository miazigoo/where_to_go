from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from adminsortable.utils import get_is_sortable

from places.models import Post, Pic


class PicsInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Pic
    readonly_fields = ["photo_preview"]

    def queryset(self, request):
        qs = super(PicsInline, self).queryset(request).filter(
            numb__icontains='foo')
        if get_is_sortable(qs):
            self.model.is_sortable = True
        else:
            self.model.is_sortable = False
        return qs

    def photo_preview(self, obj):
        return obj.photo_preview

    photo_preview.short_description = 'Photo Preview'
    photo_preview.allow_tags = True


@admin.register(Post)
class PostAdmin(SortableAdminBase, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fields = ["title", "short_description", "long_description", "lat", "lon", "point_lon", "point_lat", "slug"]
    list_display = ['pk', 'title']
    inlines = [PicsInline, ]

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )


@admin.register(Pic)
class PicAdmin(admin.ModelAdmin):
    list_display = ['sequence_number', "title", "photo_preview"]
    ordering = ['sequence_number', ]
    readonly_fields = ["photo_preview"]

    def photo_preview(self, obj):
        return obj.photo_preview

    photo_preview.short_description = 'Photo Preview'
    photo_preview.allow_tags = True
