from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from where_to_go import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('places.urls')),
    path('places/', include('endpoint.urls')),
    path('tinymce/', include('tinymce.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
