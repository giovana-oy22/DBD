from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render
from math import radians, sin, cos, sqrt, atan2

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Produto
from .models import Restaurante
from .models import Pedido
from .models import Cliente
from .models import ItemPedido


def home_web(request):
    contexto = {
        "clientes": Cliente.objects.order_by("nome"),
        "produtos": Produto.objects.select_related("restaurante").order_by("nome"),
    }
    return render(request, "painel.html", contexto)


def criar_pedido(request):
    if request.method != "POST":
        return redirect("painel")

    cliente_id = request.POST.get("cliente_id")
    produto_id = request.POST.get("produto_id")
    quantidade_raw = request.POST.get("quantidade", "1")

    try:
        quantidade = int(quantidade_raw)
        if quantidade <= 0:
            raise ValueError
    except (TypeError, ValueError):
        messages.error(request, "Quantidade invalida. Informe um inteiro maior que zero.")
        return redirect("painel")

    try:
        cliente = Cliente.objects.get(pk=cliente_id)
        produto = Produto.objects.select_related("restaurante").get(pk=produto_id)
    except (Cliente.DoesNotExist, Produto.DoesNotExist, TypeError, ValueError):
        messages.error(request, "Cliente ou produto nao encontrado.")
        return redirect("painel")

    with transaction.atomic():
        pedido = Pedido.objects.create(
            cliente=cliente,
            restaurante=produto.restaurante,
        )
        ItemPedido.objects.create(
            pedido=pedido,
            produto=produto,
            quantidade=quantidade,
        )

    messages.success(request, f"Pedido {pedido.id} criado com sucesso.")
    return redirect("painel")

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


def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371  # raio da Terra em km

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return R * c


def _listar_restaurantes_por_distancia(origem_latitude, origem_longitude):
    restaurantes = Restaurante.objects.all()
    data = []

    for restaurante in restaurantes:
        distancia = calcular_distancia(
            origem_latitude,
            origem_longitude,
            restaurante.latitude,
            restaurante.longitude,
        )

        data.append({
            "id": restaurante.id,
            "nome": restaurante.nome,
            "endereco": restaurante.endereco,
            "latitude": restaurante.latitude,
            "longitude": restaurante.longitude,
            "distancia_km": round(distancia, 3),
        })

    data.sort(key=lambda item: item["distancia_km"])
    return data


@api_view(['GET'])
def restaurantes_proximos(request):
    lat_raw = request.GET.get('lat')
    lon_raw = request.GET.get('lon')

    try:
        lat = float(lat_raw)
        lon = float(lon_raw)
    except (TypeError, ValueError):
        return Response({"detail": "Parametros lat e lon sao obrigatorios e numericos."}, status=400)

    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        return Response({"detail": "Latitude ou longitude fora da faixa valida."}, status=400)

    return Response(_listar_restaurantes_por_distancia(lat, lon))


@api_view(['GET'])
def restaurantes_proximos_cliente(request):
    cliente_id_raw = request.GET.get('cliente_id')

    try:
        cliente_id = int(cliente_id_raw)
    except (TypeError, ValueError):
        return Response({"detail": "Parametro cliente_id e obrigatorio."}, status=400)

    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        return Response({"detail": "Cliente nao encontrado."}, status=404)

    if cliente.latitude is None or cliente.longitude is None:
        return Response(
            {"detail": "Cliente sem coordenadas geograficas. Atualize o endereco cadastrado."},
            status=400,
        )

    return Response(_listar_restaurantes_por_distancia(cliente.latitude, cliente.longitude))

import requests
from django.shortcuts import render

def pagina_produtos(request):
    produtos_url = request.build_absolute_uri('/api/produtos/')
    restaurantes_url = request.build_absolute_uri('/api/restaurantes/')

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