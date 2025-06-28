from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Acao, Opcao


@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'ativo_subjacente', 'tipo', 'strike', 'vencimento')
    list_filter = ('tipo', 'vencimento')
    # search_fields = ('codigo', 'ativo_subjacente__codigo', 'ativo_subjacente__nome')

@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'setor')
    search_fields = ('codigo', 'nome', 'setor')
