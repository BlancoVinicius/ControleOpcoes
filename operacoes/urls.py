from django.contrib import admin
from django.urls import path, include
from operacoes import views


urlpatterns = [
    path('', views.get_operacoes , name="operacoes"),
    # path('opcoes/<str:codigo_acao>/', views.opcoes_por_ativo, name="opcoes_por_ativo"),
    # path('acoes/<str:codigo_acao>/', views.get_acoes, name="acoes"),

]

