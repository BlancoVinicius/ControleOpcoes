from django.db import models

# Create your models here.
from django.db import models
from ativos.models import Opcao  # ou Acao, dependendo do ativo

class Operacao(models.Model):
    TIPO_OPERACAO = (
        ('C', 'Compra'),
        ('V', 'Venda'),
    )

    data_entrada = models.DateField(null=False, blank=False)
    opcao = models.ForeignKey(Opcao, on_delete=models.PROTECT)
    tipo = models.CharField(max_length=1, choices=TIPO_OPERACAO)
    quantidade = models.PositiveIntegerField(null=False, blank=False)
    preco_entrada = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    preco_saida = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_saida = models.DateField(blank=True, null=True)
   
    def __str__(self):
        return f"{self.quantidade} {self.opcao.codigo} em {self.data_entrada}"
