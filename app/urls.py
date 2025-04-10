from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    #Path admin
    path('admin/', admin.site.urls),
    #Path core
    path('', include('core.urls')),
    #Path services
    path('', include('services.urls')),
]




if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)