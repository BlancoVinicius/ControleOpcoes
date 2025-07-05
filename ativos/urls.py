
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from ativos.views import OpcaoViewSet, AcaoViewSet

router = DefaultRouter()
router.register(r'opcoes', OpcaoViewSet)
router.register(r'acoes', AcaoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

