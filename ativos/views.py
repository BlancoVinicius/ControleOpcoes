# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

# def index(request):
#     data = {
#         "mensagem": "Olá, mundo!",
#         "status": "sucesso",
#         "valores": [1, 2, 3, 4]
#     }
#     return JsonResponse(data)
    
#     # return render(request, 'ativos/index.html')


# from django.http import JsonResponse
# from .models import Opcao

# def opcoes_por_ativo(request, codigo_acao:str):
    
#     # ao invéz do __iexact pode ser UPPERCASE
#     # cd = codigo_acao.upper()
#     # opcoes = Opcao.objects.filter(ativo_subjacente__codigo__iexact=cd)
    
#     opcoes = Opcao.objects.filter(ativo_subjacente__codigo__iexact=codigo_acao)

#     dados = []
#     for opcao in opcoes:
#         dados.append({
#             'codigo': opcao.codigo,
#             'tipo': opcao.tipo,
#             'strike': float(opcao.strike),
#             'vencimento': opcao.vencimento.strftime('%Y-%m-%d'),
#             'ativo_subjacente': opcao.ativo_subjacente.codigo,
#         })

#     return JsonResponse(dados, safe=False)

# from .models import Acao

# def get_acoes(request, codigo_acao:str):
    
#     acoes = Acao.objects.filter(codigo__iexact=codigo_acao)
    
#     dados = []
#     for acao in acoes:
#         dados.append({
#             'name': acao.nome,
#             'código': acao.codigo,
#             'setor': acao.setor,
#         })
#     return JsonResponse(dados, safe=False, json_dumps_params={'ensure_ascii': False})
    

from rest_framework import permissions, viewsets, status

from .serializers import AcaoSerializer, OpcaoSerializer, Acao, Opcao
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404


# Class para consultar opçoes e cadastrar novas opçoes
class OpcaoViewSet(viewsets.ModelViewSet):
    queryset = Opcao.objects.all()
    serializer_class = OpcaoSerializer
    #define o campo de pesquisa pelo codigo
    lookup_field = 'codigo'
    http_method_names = ['get', 'post'] 
    
    # def get_object(self):
    #     codigo = self.kwargs.get(self.lookup_field)
    #     obj = get_object_or_404(self.queryset.filter(codigo__iexact=codigo))
    #     # self.check_object_permissions(self.request, obj)
    #     return obj

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
    http_method_names = ['get', 'post'] 
    # permission_classes = [permissions.IsAuthenticated]

    