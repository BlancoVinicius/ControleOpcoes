
from django.contrib import admin
from django.urls import path, include
from ativos import views

# urlpatterns = [
#     path('',  views.index, name="index"),
#     path('opcoes/<str:codigo_acao>/', views.opcoes_por_ativo, name="opcoes_por_ativo"),
#     path('acoes/<str:codigo_acao>/', views.get_acoes, name="acoes"),

# ]

from rest_framework.routers import DefaultRouter
from .views import OpcaoViewSet, AcaoViewSet

router = DefaultRouter()
router.register(r'opcoes', OpcaoViewSet)
router.register(r'acoes', AcaoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

