from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('portafolio.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]
 

