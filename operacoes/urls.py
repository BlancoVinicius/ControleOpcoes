from django.contrib import admin
from django.urls import path, include
from operacoes import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'operacao', views.OperacaoViewSet)

urlpatterns = [
    path('', include(router.urls) , name="operacoes"),
]