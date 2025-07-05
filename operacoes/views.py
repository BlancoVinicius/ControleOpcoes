from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from operacoes.serializers import OperacaoSerializer, Operacao


class OperacaoViewSet(viewsets.ModelViewSet):
    queryset = Operacao.objects.all()
    serializer_class = OperacaoSerializer
    http_method_names = ['get', 'post', 'put']
    lookup_field = 'opcao__codigo'