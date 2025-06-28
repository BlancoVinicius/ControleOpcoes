# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    data = {
        "mensagem": "Olá, mundo!",
        "status": "sucesso",
        "valores": [1, 2, 3, 4]
    }
    return JsonResponse(data)
    
    # return render(request, 'ativos/index.html')


from django.http import JsonResponse
from .models import Opcao

def opcoes_por_ativo(request, codigo_acao:str):
    
    # ao invéz do __iexact pode ser UPPERCASE
    # cd = codigo_acao.upper()
    # opcoes = Opcao.objects.filter(ativo_subjacente__codigo__iexact=cd)
    
    opcoes = Opcao.objects.filter(ativo_subjacente__codigo__iexact=codigo_acao)

    dados = []
    for opcao in opcoes:
        dados.append({
            'codigo': opcao.codigo,
            'tipo': opcao.tipo,
            'strike': float(opcao.strike),
            'vencimento': opcao.vencimento.strftime('%Y-%m-%d'),
            'ativo_subjacente': opcao.ativo_subjacente.codigo,
        })

    return JsonResponse(dados, safe=False)

from .models import Acao

def get_acoes(request, codigo_acao:str):
    
    acoes = Acao.objects.filter(codigo__iexact=codigo_acao)
    
    dados = []
    for acao in acoes:
        dados.append({
            'name': acao.nome,
            'código': acao.codigo,
            'setor': acao.setor,
        })
    return JsonResponse(dados, safe=False, json_dumps_params={'ensure_ascii': False})
    