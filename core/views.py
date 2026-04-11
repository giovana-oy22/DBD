from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Produto
from .models import Restaurante
from .models import Pedido

from math import sqrt

@api_view(['GET'])
def lista_produtos(request):
    produtos = Produto.objects.all()

    data = []
    for p in produtos:
        data.append({
            "id": p.id,
            "nome": p.nome,
            "preco": float(p.preco),
            "restaurante": p.restaurante.nome
        })

    return Response(data)

@api_view(['GET'])
def lista_restaurantes(request):
    restaurantes = Restaurante.objects.all()

    data = []
    for r in restaurantes:
        data.append({
            "id": r.id,
            "nome": r.nome,
            "endereco": r.endereco,
            "latitude": r.latitude,
            "longitude": r.longitude
        })

    return Response(data)

@api_view(['GET'])
def lista_pedidos(request):
    pedidos = Pedido.objects.all()

    data = []
    for p in pedidos:
        itens = []
        total = 0

        for item in p.itempedido_set.all():
            subtotal = item.quantidade * item.produto.preco
            total += subtotal

            itens.append({
                "produto": item.produto.nome,
                "quantidade": item.quantidade,
                "subtotal": float(subtotal)
            })

        data.append({
            "id": p.id,
            "cliente": p.cliente.nome,
            "restaurante": p.restaurante.nome,
            "data": p.data,
            "total": float(total),
            "itens": itens
        })

    return Response(data)

@api_view(['GET'])
def restaurantes_proximos(request):
    lat = float(request.GET.get('lat'))
    lon = float(request.GET.get('lon'))

    restaurantes = Restaurante.objects.all()
    data = []

    for r in restaurantes:
        distancia = sqrt(
            (r.latitude - lat) ** 2 +
            (r.longitude - lon) ** 2
        )

        data.append({
            "id": r.id,
            "nome": r.nome,
            "distancia": distancia
        })

    data.sort(key=lambda x: x["distancia"])

    return Response(data)

import requests
from django.shortcuts import render

def pagina_produtos(request):
    produtos_url = 'http://localhost:8001/api/produtos/'
    restaurantes_url = 'http://localhost:8001/api/restaurantes/'

    query_produto = request.GET.get('produto')
    query_restaurante = request.GET.get('restaurante')

    try:
        produtos_resp = requests.get(produtos_url, timeout=3)
        restaurantes_resp = requests.get(restaurantes_url, timeout=3)

        produtos = produtos_resp.json() if produtos_resp.status_code == 200 else []
        restaurantes = restaurantes_resp.json() if restaurantes_resp.status_code == 200 else []

    except:
        produtos = []
        restaurantes = []

    # 🔍 FILTRO POR PRODUTO
    if query_produto:
        produtos = [
            p for p in produtos
            if query_produto.lower() in p['nome'].lower()
        ]

    # 🔍 FILTRO POR RESTAURANTE
    if query_restaurante:
        produtos = [
            p for p in produtos
            if query_restaurante.lower() in p['restaurante'].lower()
        ]

    return render(request, 'core/produtos.html', {
        'produtos': produtos,
        'restaurantes': restaurantes,
        'query_produto': query_produto,
        'query_restaurante': query_restaurante
    })