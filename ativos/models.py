from django.db import models

from django.db import models

class AtivoBase(models.Model):
    codigo = models.CharField(max_length=20, unique=True, blank=False, null=False)
    nome = models.CharField(max_length=100, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Acao(AtivoBase):
    setor = models.CharField(max_length=50, blank=True, null=True)
    sub_setor = models.CharField(max_length=50, blank=True, null=True)

class Opcao(AtivoBase):
    MOD_CHOICES = [
        ('AME', 'Americana'),
        ('EUR', 'Européia'),
    ]

    TIPO_CHOICES = [
        ('CALL', 'Call'),
        ('PUT', 'Put'),
    ]
    
    ativo_subjacente = models.ForeignKey(Acao, on_delete=models.PROTECT, related_name='opcoes', blank=False,null=False)
    tipo = models.CharField(max_length=4, choices=TIPO_CHOICES, blank=False, null=False)
    modelo = models.CharField(max_length=3, choices=MOD_CHOICES, blank=False, null=False)
    strike = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    vencimento = models.DateField(blank=False, null=False)

    class Meta:
        unique_together = ('ativo_subjacente', 'tipo', 'strike', 'vencimento', 'codigo')