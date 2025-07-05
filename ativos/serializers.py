from rest_framework import serializers
from .models import Acao, Opcao

class AcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acao
        fields = '__all__'

class OpcaoSerializer(serializers.ModelSerializer):
    
    ativo_subjacente = serializers.StringRelatedField(source='ativo_subjacente.nome', read_only=True)

    ativo_subjacente = serializers.SlugRelatedField(
        queryset=Acao.objects.all(),
        slug_field='codigo'
    )
    class Meta:
        model = Opcao
        fields = '__all__'
        # fields = ['codigo', 'nome', 'strike', 'ativo_subjacente', 'modelo', 'tipo', 'vencimento']

