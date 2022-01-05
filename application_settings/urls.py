from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('mainApp.urls')),
    path('api/v1/', include('routes')),
    path('', include('oauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
