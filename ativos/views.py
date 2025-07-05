from rest_framework import permissions, viewsets, status
from .serializers import AcaoSerializer, OpcaoSerializer, Acao, Opcao
from rest_framework.decorators import action
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404


class OpcaoViewSet(viewsets.ModelViewSet):
    queryset = Opcao.objects.all()
    serializer_class = OpcaoSerializer
    lookup_field = 'codigo' #define o campo de pesquisa pelo codigo
    http_method_names = ['get', 'post', 'put']
    
    #url para pesquisa de opçoes por ativo base http://127.0.0.1:8000/api/opcoes/filtrar-por-ativo/BBAS3/
    @action(detail=False, methods=['get'], url_path='filtrar-por-ativo/(?P<codigo_ativo>[^/.]+)')
    def filtrar_por_ativo(self, request, codigo_ativo=None):
        opcoes = self.queryset.filter(ativo_subjacente__codigo__iexact=codigo_ativo)
        serializer = self.get_serializer(opcoes, many=True)
        return Response(serializer.data)

class AcaoViewSet(viewsets.ModelViewSet):

    queryset = Acao.objects.all()
    serializer_class = AcaoSerializer
    lookup_field = 'codigo'
    http_method_names = ['get', 'post', 'put'] 