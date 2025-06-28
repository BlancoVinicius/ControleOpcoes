from django.db import models

# Create your models here.
from django.db import models

class AtivoBase(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Acao(AtivoBase):
    setor = models.CharField(max_length=50, blank=True, null=True)
    # você pode adicionar campos específicos de ação, se precisar

class Opcao(AtivoBase):
    TIPO_CHOICES = [
        ('CALL', 'Call'),
        ('PUT', 'Put'),
    ]
    ativo_subjacente = models.ForeignKey(Acao, on_delete=models.CASCADE, related_name='opcoes')
    tipo = models.CharField(max_length=4, choices=TIPO_CHOICES)
    strike = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()

    class Meta:
        unique_together = ('ativo_subjacente', 'tipo', 'strike', 'vencimento')