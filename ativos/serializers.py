from rest_framework import serializers
from .models import Acao, Opcao

class AcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acao
        fields = ['codigo', 'nome']

class OpcaoSerializer(serializers.ModelSerializer):
    
    ativo_subjacente = serializers.StringRelatedField(source='ativo_subjacente.nome', read_only=True)

    # escrita (espera o código da ação no POST)
    ativo_subjacente = serializers.SlugRelatedField(
        queryset=Acao.objects.all(),
        slug_field='codigo'
    )
    class Meta:
        model = Opcao
        fields = ['codigo', 'nome', 'strike', 'ativo_subjacente', 'modelo', 'tipo', 'vencimento']

