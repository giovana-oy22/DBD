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