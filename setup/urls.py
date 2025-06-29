
from django.contrib import admin
from django.urls import path, include

from ativos.urls import router as seu_app_router

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('ativos/', include('ativos.urls')),
    path('api/', include(seu_app_router.urls)),
    path('operacoes/', include('operacoes.urls')),

] 

#Durante desenvolvimento para servir envio de arquivos staticos
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)