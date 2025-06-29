from rest_framework import serializers
from .models import Operacao, Opcao

class OperacaoSerializer(serializers.ModelSerializer):
    
    ativo_subjacente = serializers.CharField(source='opcao.ativo_subjacente.codigo', read_only=True)
    
    opcao = serializers.SlugRelatedField(
        queryset=Opcao.objects.all(),
        slug_field='codigo'
    )

    # ativo_subjacente = serializers.SlugRelatedField(
    #     queryset=Operacao.objects.all(),
    #     slug_field='codigo'
    # )
    class Meta:
        model = Operacao
        fields = '__all__'
    