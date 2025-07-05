
from django.contrib import admin
from django.urls import path, include

from ativos.urls import router as ativos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(ativos.urls)),
    path('operacoes/', include('operacoes.urls')),

] 

#Durante desenvolvimento para servir envio de arquivos staticos
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)