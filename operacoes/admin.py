from django.contrib import admin
from .models import Operacao

# Register your models here.

@admin.register(Operacao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ('data_entrada', 'tipo', 'quantidade', 'preco_entrada', 'preco_saida', 'data_saida')
    
